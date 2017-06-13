from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from .models import Question
# Create your views here.

def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': lastest_question_list,
    }
    # output = ', '.join([p.question_text for p in lastest_question_list])
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse('You are looking at question %s.' % question_id)


def results(request, question_id):
    response = 'you are looking at the results of question. %s'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You are voting on question %s.' % question_id)