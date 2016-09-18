from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'main.views.home', name= 'home'),
    url(r'^about$', 'main.views.about', name= 'about'),
    url(r'^article/(?P<article_id>[0-9]+)/$', 'main.views.show_article', name= 'article'),
)