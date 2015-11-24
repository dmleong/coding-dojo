from django.conf.urls import patterns, url
from apps.ninja import views
urlpatterns = patterns('',
    url(r'^$', views.all, name='all'),
    url(r'^(?P<color>\w+)/$', views.ninja, name='ninja'),
)
