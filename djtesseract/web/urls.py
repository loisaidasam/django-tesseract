from django.conf.urls.defaults import *

urlpatterns = patterns('djtesseract.web.views',
	url(r'^ocr/$', 'ocr', name='ocr'),
	url(r'^$', 'index', name='index'),
)
