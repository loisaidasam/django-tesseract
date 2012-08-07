
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def _return_response(response_dict, status=200):
	response = json.dumps(response_dict)
	return HttpResponse(response, status=status, content_type="application/javascript")


@csrf_exempt
def ocr(request):
	return _return_response({})
