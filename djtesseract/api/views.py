
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from djtesseract.web.forms import handle_uploaded_file, OCRForm


def _return_response(response_dict, status=200):
	response = json.dumps(response_dict)
	return HttpResponse(response, status=status, content_type="application/javascript")


@csrf_exempt
def ocr(request):
	if request.method != 'POST':
		return _return_response({'message': "POST required"}, 404)
	
	form = OCRForm(request.POST, request.FILES)
	if not form.is_valid():
		return _return_response({'message': "%s" % form.errors}, 404)
	
	result = handle_uploaded_file(request.FILES['file'])
	
	return _return_response({'result': result})
	
	'''
	putting this here because we basically want "Content-type: application/x-www-form-urlencoded"
	from facebook:
// Create a new album
$graph_url = "https://graph.facebook.com/me/albums?"
. "access_token=". $access_token;

$postdata = http_build_query(
array(
 'name' => $album_name,
 'message' => $album_description
   )
 );
$opts = array('http' =>
array(
 'method'=> 'POST',
 'header'=>
   'Content-type: application/x-www-form-urlencoded',
 'content' => $postdata
 )
);
$context  = stream_context_create($opts);
$result = json_decode(file_get_contents($graph_url, false, 
  $context));
	'''
