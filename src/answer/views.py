from datetime import timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.views import LoginView

from .models import Question, Answer, Upvote


class QuestionListView(ListView):
    model = Question


class QuestionDetailView(DetailView):
    model = Question
    context_object_name = 'question'

    def post(self, request, *args, **kwargs):
        print(request.POST)
        if request.POST['type'] == 'vote':
            ans = Answer.objects.get(id=request.POST['answer_id'])
            if request.user.is_authenticated:
                if request.POST['vote'][0:1] == 'U':
                    upvote = Upvote.objects.get_or_create(answers=ans, user=request.user)
                elif request.POST['vote'][0:1] == 'D':
                    upvote = Upvote.objects.filter(answers=ans, user=request.user).delete()

            # if not logged in
        return HttpResponseRedirect(f'/question/{ans.questions.id}')


# class AnswerByMeListView(ListView):
#     template_name = 'answer/myanswer.html'
#
#     def get_queryset(self):
#         print(Answer.objects.filter(user=self.request.user))
#         return Answer.objects.filter(user=self.request.user)
#
#     # def my_answer(self):
#     #     print(self.get_context_data())
#     #     return Answer.objects.filter(user=self.request.user)
#     #
#

class AnswerByMeListView(LoginRequiredMixin, ListView):
    model = Answer
    template_name = 'answer/myanswer.html'
    login_url = '/login'
    redirect_field_name = 'next'

    # def get_context_data(self, **kwargs):
    #     context = super(AnswerByMeListView, self).get_context_data(**kwargs)
    #     context['pk'] = self.kwargs['pk']
    #     return context

    def get_queryset(self):
        return Answer.objects.filter(user=self.request.user)


class MyQuestionView(LoginRequiredMixin, TemplateView):
    template_name = 'answer/myquestions.html'

    def my_question(self):
        return Question.objects.filter(user=self.request.user)


class MyUpvoteView(LoginRequiredMixin, TemplateView):
    template_name = 'answer/my_upvotes.html'

    def my_upvotes(self):
        return Upvote.objects.filter(user=self.request.user)


class QuestionOfTheHour(LoginRequiredMixin, TemplateView):
    template_name = 'answer/question_of_the_hour.html'

    def question_of_the_hour(self):
        last_hour_questions = Answer.objects.filter(pub_date__gte=timezone.now() - timedelta(hours=1))
        best_question = last_hour_questions[0]
        old_vote = 0
        for ans in best_question.answer_set.all():
            old_vote += ans.upvote_set.all().count()

        for question in Question.objects.all():
            vote = 0
            for ans in question.answer_set.all():
                vote += ans.upvote_set.all().count()
            if vote > old_vote:
                best_question = question
        return best_question


class QuestionOfTheSiteView(LoginRequiredMixin, TemplateView):
    template_name = 'answer/question_of_the_site.html'

    def question_of_the_site(self):
        best_question = Question.objects.first()
        old_vote = 0
        for ans in best_question.answer_set.all():
            old_vote += ans.upvote_set.all().count()

        for question in Question.objects.all():
            vote = 0
            for ans in question.answer_set.all():
                vote += ans.upvote_set.all().count()
            if vote > old_vote:
                best_question = question
        return best_question
