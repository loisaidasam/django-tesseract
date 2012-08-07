from django.conf.urls.defaults import *

urlpatterns = patterns('djtesseract.api.views',
	url(r'^ocr/', 'ocr', name='ocr'),
)
