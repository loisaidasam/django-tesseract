
from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
	# API
	(r'^api/', include('djtesseract.api.urls')),
	
	# Web
	(r'', include('djtesseract.web.urls')),
)
