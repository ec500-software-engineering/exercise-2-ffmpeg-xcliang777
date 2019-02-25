import subprocess
import json
import pytest
from main import ffmpeg

def test_duration(filein):
	""" get media metadata """
	meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                	'-print_format', 'json',
                                	'-show_streams',
                                	'-show_format',
                                	str(filein)],
                               	text=True)
	meta_test = json.loads(meta)
	duration_test = float(meta_test['streams'][0]['duration'])
	assert duration_test == pytest.approx(5.)

	return duration_test