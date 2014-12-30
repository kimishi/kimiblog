#!/usr/bin/env python
# coding=utf-8

from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
     # ex: /polls/
     url(regex = r'^$', view = views.index, name = 'index'),
     # ex /polls/5/
     url(regex = r'^(?P<question_id>\d+)/$', view = views.detail, name='detail'),
     # ex: /polls/5/results/
     url(regex = r'^(?P<question_id>\d+)/results/$', view = views.results, name='results'),
     # ex: /polls/5/vote/
     url(regex = r'^(?P<question_id>\d+)/vote/$', view = views.vote, name='vote'),
     )

