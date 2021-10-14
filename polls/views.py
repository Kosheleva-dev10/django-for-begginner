from django.http import HttpResponse
from .models import Question
from .models import Choice
from django.urls import reverse
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect


from django.shortcuts import get_object_or_404, render


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    
# Other way(using shortcuts)
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.hmtml', context)
    

def detail(request, question_id):
    template = loader.get_template('polls/detail.html')
    question = Question.objects.get(pk=question_id)
    context = {
        'question': question,
    }
    return HttpResponse(template.render(context, request))
    

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

