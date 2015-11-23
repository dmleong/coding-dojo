from django.conf.urls import patterns, url
from apps.quiz import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/$', views.show, name='show'),
)

