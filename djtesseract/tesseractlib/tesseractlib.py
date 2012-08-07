
import logging
import os
import time

from django.conf import settings
from fabric.api import local, put, run
from fabric.api import settings as fab_settings

logger = logging.getLogger(__name__)


def ocr_from_file(filename):
	
	# Local tesseract
	if settings.TESSERACT_LOCAL:
		cmd = "tesseract '%s' outfile" % filename
		logger.info("Running tesseract-ocr locally: %s" % cmd)
		result = local(cmd)
		logger.debug(result)
		
		cmd = "cat outfile.txt"
		logger.info("Getting results of tesseract-ocr: %s" % cmd)
		end_result = run(cmd)
		logger.debug(result)
		
		cmd = "rm outfile.txt"
		logger.info("Removing local output file: %s" % cmd)
		result = local(cmd)
		logger.debug(result)
		
		return end_result
	
	# Remote tesseract
	host_string = settings.TESSERACT_HOST
	if settings.TESSERACT_USERNAME:
		host_string = "%s@%s" % (settings.TESSERACT_USERNAME, host_string)
	if settings.TESSERACT_PORT:
		host_string = "%s:%s" % (host_string, settings.TESSERACT_PORT)
	logger.info("Running tesseract-ocr remotely on host %s" % host_string)
	
	with fab_settings(host_string=host_string):
		# We must do this in case they don't fill in this value
		if settings.TESSERACT_REMOTE_TMP_DIR:
			dir_prefix = "%s/" % settings.TESSERACT_REMOTE_TMP_DIR
		else:
			dir_prefix = ""
		
		if dir_prefix:
			cmd = "mkdir -p %s" % dir_prefix
			logger.info("Making sure temporary directory is on remote host: %s" % cmd)
			result = run(cmd)
			logger.debug(result)
		
		remote_filename = os.path.basename(filename)
		logger.info("Copying %s to remote host as %s ..." % (filename, remote_filename))
		result = put(filename, "%s%s" % (dir_prefix, remote_filename))
		logger.debug(result)
		logger.info("OK")
	
		cmd = "tesseract %s%s %soutfile" % (dir_prefix, remote_filename, dir_prefix)
		logger.info("Running tesseract-ocr: %s" % cmd)
		result = run(cmd)
		logger.debug(result)
		
		cmd = "cat %soutfile.txt" % dir_prefix
		logger.info("Getting results of tesseract-ocr: %s" % cmd)
		end_result = run(cmd)
		logger.debug(result)
		
		cmd = "rm %s%s" % (dir_prefix, remote_filename)
		logger.info("Removing temporary file: %s" % cmd)
		result = run(cmd)
		logger.debug(result)
		
		cmd = "rm %soutfile.txt" % dir_prefix
		logger.info("Removing temporary outfile: %s" % cmd)
		result = run(cmd)
		logger.debug(result)
		
		return end_result
