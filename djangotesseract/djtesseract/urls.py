
from django.conf.urls.defaults import *
from django.conf import settings

my_patterns = [
	url(r'^api/', 'api', name='api'),
]

if settings.TESSERACT_ENABLE_WEB:
	my_patterns += [
		url(r'^web/', 'web', name='web'),
		url(r'^apidocs/', 'apidocs', name='apidocs'),
		url(r'^$', 'index', name='index'),
	]

urlpatterns = patterns('djangotesseract.djtesseract.views',
	*my_patterns
)
