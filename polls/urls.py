#!/usr/bin/env python
# coding=utf-8

from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
     # ex: /polls/
     url(regex = r'^$', view = views.IndexView.as_view(), name = 'index'),
     # ex /polls/5/
     url(regex = r'^(?P<pk>\d+)/$', view = views.DetailView.as_view(), name='detail'),
     # ex: /polls/5/results/
     url(regex = r'^(?P<pk>\d+)/results/$', view = views.ResultsView.as_view(), name='results'),
     # ex: /polls/5/vote/
     url(regex = r'^(?P<question_id>\d+)/vote/$', view = views.vote, name='vote'),
     )

