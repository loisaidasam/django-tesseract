
from django.shortcuts import render_to_response
from django.template import RequestContext

from djtesseract.web.forms import handle_uploaded_file, OCRForm


def index(request):
	context = {'tab_name': 'index'}
	return render_to_response('index.html', context, context_instance=RequestContext(request))

def ocr(request):
	context = {
		'tab_name': 'ocr',
		'ocr_result': None,
	}
	if request.method == 'POST':
		form = OCRForm(request.POST, request.FILES)
		if form.is_valid():
			context['ocr_result'] = handle_uploaded_file(request.FILES['img_file'])
	else:
		form = OCRForm()
	
	context['form'] = form
	return render_to_response('ocr.html', context, context_instance=RequestContext(request))