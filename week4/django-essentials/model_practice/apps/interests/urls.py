from django.conf.urls import patterns, url
from apps.interests import views

urlpatterns = patterns('',
    url(r'^$', views.show_interests, name='show_interests'),
    url(r'^(?P<id>\d+)', views.show_user, name='show_user'),
)

