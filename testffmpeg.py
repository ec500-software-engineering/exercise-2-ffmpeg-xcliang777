import pytest
from main import main


def test_ffmpeg():
	dur = await main()
	assert dur == pytest.approx(5.)

if __name__ == '__main__':
    pytest.main(['-x',__file__])