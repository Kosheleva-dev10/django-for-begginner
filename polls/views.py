from django.http import HttpResponse
from .models import Question
from .models import Choice

# import django.shortcuts import render

from django.template import loader


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
    print('======question_id: =======', question_id)
    template = loader.get_template('polls/detail.html')
    question = Question.objects.get(pk=question_id)
    context = {
        'question': question,
    }
    print("template: ", template, "context: ", context )
    return HttpResponse(template.render(context, request))
    

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
