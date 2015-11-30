"""generic_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from apps.school.views import Subjects, TeachersDetailView, TeachersListView
from apps.school.views import StudentsListView, StudentsDetailView
from apps.school.views import SubjectsDetailView

urlpatterns = patterns(
    '',
    url(r'^$', Subjects.as_view(), name='subjects'),
    url(r'^teachers/(?P<pk>[-_\w]+)/$',
        TeachersDetailView.as_view(),
        name='teacher-detail',
        ),
    url(r'^students/(?P<pk>[-_\w]+)/$',
        StudentsDetailView.as_view(),
        name='student-detail',
        ),
    url(r'^subjects/(?P<pk>[-_\w]+)/$',
        SubjectsDetailView.as_view(),
        name='subject-detail',
        ),
    url(r'^teachers/$', TeachersListView.as_view(), name='teacher-list'),
    url(r'^students/$', StudentsListView.as_view(), name='student-list'),
    url(r'^admin/', include(admin.site.urls)),
)
