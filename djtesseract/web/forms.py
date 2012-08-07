
import logging
import os
import time

from django import forms
from django.conf import settings

import djtesseract.tesseractlib.tesseractlib as tesseractlib

logger = logging.getLogger(__name__)


def handle_uploaded_file(f):
	filedir = "%s/%s" % (settings.MEDIA_ROOT, time.time())
	logger.info("Step 1. Making temporary directory at %s ..." % filedir)
	os.mkdir(filedir)
	logger.info("OK")
	
	filename = "%s/%s" % (filedir, int(time.time()))
	logger.info("Step 2. Creating file at %s ..." % filename)
	with open(filename, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
	logger.info("OK")
	
	logger.info("Step 3. Running OCR on file at %s ..." % filename)
	try:
		result = tesseractlib.ocr_from_file(filename)
		logger.info("OK")
	except Exception, e:
		logger.error("Exception caught when running tesseract-ocr: %s" % e)
		result = "Error: %s" % e
	
	logger.info("Step 4. Removing file at %s ..." % filename)
	os.remove(filename)
	logger.info("OK")
	
	logger.info("Step 5. Removing temporary directory at %s ..." % filedir)
	os.rmdir(filedir)
	logger.info("OK")
	
	return result


class OCRForm(forms.Form):
	file = forms.FileField(label='Select a file')