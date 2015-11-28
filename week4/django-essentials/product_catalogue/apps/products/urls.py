"""model_practice URL Configuration

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
from django.conf.urls import patterns, url
from apps.products import views

urlpatterns = patterns('',
    url(r'^create_product', views.create_product, name='create_product'),
    url(r'^edit/(?P<id>\d+)$', views.edit_product, name='edit_product'),
    url(r'^update/(?P<id>\d+)$', views.update_product, name='update_product'),
    url(r'^delete/(?P<id>\d+)$', views.delete_product, name='delete_product'),
)

