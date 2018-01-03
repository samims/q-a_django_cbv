from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Question, Answer


class QuestionListView(ListView):
    model = Question


class QuestionDetailView(DetailView):
    model = Question
    context_object_name = 'question'


class AnswerByMeListView(ListView):
    model = Answer
    template_name = 'answer/myanswer.html'

    # def get_context_data(self, **kwargs):
    #     context = super(AnswerByMeListView, self).get_context_data(**kwargs)
    #     print(self.kwargs)
    #     context['pk'] = self.kwargs['pk']
    #
    #     return context

    def get_queryset(self):
        return Answer.objects.filter(pk=self.kwargs['pk'])
