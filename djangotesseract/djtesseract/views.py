
import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from djangotesseract.djtesseract.forms import handle_uploaded_file, OCRForm


def index(request):
	context = {'tab_name': 'index'}
	return render_to_response('index.html', context, context_instance=RequestContext(request))


def web(request):
	context = {'tab_name': 'web'}
	
	if request.method == 'POST':
		form = OCRForm(request.POST, request.FILES)
		if form.is_valid():
			context['got_ocr_result'] = True
			context['ocr_result'] = handle_uploaded_file(request.FILES['file'])
	else:
		form = OCRForm()
	
	context['form'] = form
	return render_to_response('ocr.html', context, context_instance=RequestContext(request))


def _return_response(response_dict, status=200):
	response = json.dumps(response_dict)
	return HttpResponse(response, status=status, content_type="application/javascript")


@csrf_exempt
def api(request):
	if request.method != 'POST':
		return _return_response({'message': "POST required"}, 404)
	
	form = OCRForm(request.POST, request.FILES)
	if not form.is_valid():
		err_label = form.errors.iterkeys().next()
		err_reason = form.errors[err_label][0]
		return _return_response({'message': "%s: %s" % (err_label, err_reason)}, 404)
	
	result = handle_uploaded_file(request.FILES['file'])
	
	return _return_response({'result': result})
