from django.http import HttpResponse
from django.shortcuts import render

from .models import Question, Choice

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question for q in question_list])
    return HttpResponse(output)

def detail(req, question_id):
    return HttpResponse("Question: %s" % question_id)

def vote(req, question_id):
    return HttpResponse("Voting on question: %s" % question_id)

def results(req, question_id):
    return HttpResponse("Results for question: %s" % question_id)
