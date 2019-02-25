import pytest
import os
from main import re_encode_video


def test_ffmpeg():
	for file in os.listdir("./"):
		if file.endswith('.mp4'):
			dur = re_encode_video(file)
			assert dur == pytest.approx(5.)

if __name__ == '__main__':
    pytest.main(['-x',__file__])