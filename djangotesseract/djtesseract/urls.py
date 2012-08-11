from django.conf.urls.defaults import *

urlpatterns = patterns('djangotesseract.djtesseract.views',
	url(r'^api/', 'api', name='api'),
	url(r'^web/', 'web', name='web'),
	url(r'^$', 'index', name='index'),
)
