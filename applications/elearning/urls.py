# -*- coding: utf-8 -*
from django.conf.urls import url, include

from . import views
from django.views import generic
from django.views.decorators.cache import cache_page
from applications.elearning.views import course_crud as views
from applications.elearning.views import views_general as gviews
__author__ = 'Guinsly'


urlpatterns = [

   url(r'^create/$', views.CourseCreateView.as_view(), name='course_create'),
   url(r'^update/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name='course_update'),
   url(r'^detail/(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='course_detail'),
   url(r'^delete/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name='course_delete'),
   url(r'^$', views.CourseListView.as_view(), name='courses_home'),
   url(r'^$', views.CourseListView.as_view(), name='index'),


      #url(r'^(?P<pk>[0-9]+)/$', views.CourseDetailView.as_view(), name='course-detail'),

      # url(r'^$', views.HomeView.as_view(), name='index'),
      url(r'^dashboard/$', gviews.DashBoard.as_view(), name='index'),

        ]


