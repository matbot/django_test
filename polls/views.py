from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import Http404, get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # potential race condition; see: https://docs.djangoproject.com/en/3.0/ref/models/expressions/#avoiding-race
        # -conditions-using-f
        selected_choice = question.choice_set.get(pk=req.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redirect back to input form.
        return render(req, 'polls/detail.html', {'question': question, 'error_message': "No choice selected."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# def index(request):
#     question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': question_list
#     }
#     # output = ', '.join([q.question for q in question_list])
#     return render(request, 'polls/index.html', context)
#
#
# def detail(req, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Requested question does not exist.")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(req, 'polls/detail.html', {'question': question})
#
#
# def vote(req, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         # potential race condition; see: https://docs.djangoproject.com/en/3.0/ref/models/expressions/#avoiding-race
#         # -conditions-using-f
#         selected_choice = question.choice_set.get(pk=req.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # redirect back to input form.
#         return render(req, 'polls/detail.html', {'question': question, 'error_message': "No choice selected."})
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
#
#
# def results(req, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(req, 'polls/results.html', {'question': question})
