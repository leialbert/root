from django.http.response import Http404
from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

from polls.models import Question

def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list':lastest_question_list,
    }
    return render(request,'polls/index.html',context)


def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    context = {
        'question':question,
    }

    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

