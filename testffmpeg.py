import pytest
from main import ffmpeg


def test_ffmpeg():
	dur = ffmpeg()
	assert dur == pytest.approx(5.)

if __name__ == '__main__':
    pytest.main(['-x',__file__])