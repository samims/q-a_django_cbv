from .views import QuestionListView, QuestionDetailView, AnswerByMeListView

from django.conf.urls import url

urlpatterns = [
    url(r'^$', QuestionListView.as_view(), name='home'),
    url(r'^(?P<pk>\d+)/$', QuestionDetailView.as_view(), name='detail'),
    url(r'^answers/(?P<pk>\d+)/$', AnswerByMeListView.as_view(), name='answer_by_me' )
]
