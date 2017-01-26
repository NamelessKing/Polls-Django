from django.http import HttpResponse
from django.shortcuts import render
from.models import Question
# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5].reverse()
    print(latest_questions)
    context = {'latest_questions':latest_questions}
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    question = Question.objects.get(pk = question_id)
    return render(request,'polls/detail.html',{'question': question})

def results(request,question_id):
    return HttpResponse('result of question: %s' % question_id)

def vote(request,question_id):
    return HttpResponse('vote on questions %s' % question_id)