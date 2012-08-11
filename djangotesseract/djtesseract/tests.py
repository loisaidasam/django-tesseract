
import json
import os

from django.test import TestCase

import djangotesseract.djtesseract.tesseractlib as tesseractlib

class LibTest(TestCase):
    def test_lib(self):
    	filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures', 'test.png')
    	result = tesseractlib.ocr_from_file(filename)
    	self.assertEqual(result, 'Tesseract-OCR')


class APITest(TestCase):
	def test_api_request(self):
		filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures', 'test.png')
		
		with open(filename, 'r') as fp:
			response = self.client.post("/api/", {'file': fp})
		
		self.assertEqual(response.status_code, 200)
		
		json_result = json.loads(response.content)
		
		self.assertEqual(json_result, {'result': 'Tesseract-OCR'})


class WebTest(TestCase):
	def test_web(self):
		response = self.client.get("/")
		self.assertEqual(response.status_code, 200)
		
		response = self.client.get("/web/")
		self.assertEqual(response.status_code, 200)
