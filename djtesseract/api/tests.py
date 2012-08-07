
import json
import os

from django.test import TestCase


class APITest(TestCase):
	def test_api_request(self):
		filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../fixtures', 'test.png')
		
		with open(filename, 'r') as fp:
			response = self.client.post("/api/ocr/", {'file': fp})
		
		self.assertEqual(response.status_code, 200)
		
		json_result = json.loads(response.content)
		
		self.assertEqual(json_result, {'result': 'Tesseract-OCR'})
		
