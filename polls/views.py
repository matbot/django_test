from django.http import HttpResponse
from django.template import loader
from django.shortcuts import Http404, get_object_or_404, render

from .models import Question, Choice


# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': question_list
    }
    # output = ', '.join([q.question for q in question_list])
    return render(request, 'polls/index.html', context)


def detail(req, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Requested question does not exist.")
    question = get_object_or_404(Question, pk=question_id)
    return render(req, 'polls/detail.html', {'question': question})


def vote(req, question_id):
    return HttpResponse("Voting on question: %s" % question_id)


def results(req, question_id):
    return HttpResponse("Results for question: %s" % question_id)
