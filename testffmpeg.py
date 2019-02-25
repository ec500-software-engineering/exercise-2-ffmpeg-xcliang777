import pytest
import os
from main import re_encode_video

def test_ffmpeg(file):
	dur = re_encode_video(file)
	assert dur == pytest.approx(1.)

if __name__ == '__main__':
    pytest.main(['-x',__file__])