# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.decorators.cache import cache_page
from django.conf.urls import url, include, handler404, handler500
admin.autodiscover()

from applications.elearning.views.views_crud import robot_files

urlpatterns = [
	#Robot and Humans.txt
	url(
		r'^(?P<filename>(robots.txt)|(humans.txt))$', 
		robot_files, 
        name='home-files'
		),
	
	#Main application
    url(
    	r'^elearning/', 
    	include(
    	    'applications.elearning.urls', 
    		namespace="elearning"
    	   )
    	),
    url(r'^', include('applications.elearning.urls')),
    
    #admin
    url(r'^admin/', 
        include('admin_honeypot.urls', 
            namespace='admin_honeypot')
        ),
    url(r'^ilovemyself/', include(admin.site.urls)),
]

#handler404 = 'applications.elearning.views.views_crude.handler404'
#handler500 = 'applications.elearning.views.views_crude.handler500'