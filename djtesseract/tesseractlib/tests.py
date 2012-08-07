

import os
def next_to_this_file(additional_path, this_file = __file__):
	return os.path.join(os.path.dirname(os.path.abspath(this_file)), additional_path)

from django.test import TestCase

import djtesseract.tesseractlib.tesseractlib as tesseractlib


class OCRTest(TestCase):
    def test_ocr(self):
    	filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures', 'test.png')
    	result = tesseractlib.ocr_from_file(filename)
    	self.assertEqual(result, 'Tesseract-OCR')