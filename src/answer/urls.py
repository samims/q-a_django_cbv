from .views import QuestionListView, QuestionDetailView, AnswerByMeListView, MyQuestionView, MyUpvoteView, \
    QuestionOfTheSiteView, QuestionOfTheHour

from django.conf.urls import url

urlpatterns = [
    url(r'^$', QuestionListView.as_view(), name='home'),
    url(r'^(?P<pk>\d+)/$', QuestionDetailView.as_view(), name='detail'),
    url(r'^myanswers/$', AnswerByMeListView.as_view(), name='my_answers'),
    url(r'^myquestions/(?P<pk>\d)/$', MyQuestionView.as_view(), name='my_questions'),
    url(r'^myupvotes/$', MyUpvoteView.as_view(), name='my_upvotes'),
    url(r'^questionofthesite/$', QuestionOfTheSiteView.as_view(), name='question_of_the_site'),
    url(r'questionofthehour/$', QuestionOfTheHour.as_view(), name='question_of_the_hour')
]
