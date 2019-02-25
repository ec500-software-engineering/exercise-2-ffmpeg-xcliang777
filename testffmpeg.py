import pytest
from main import re_encode_video

@pytest.mark.asyncio
async def test_ffmpeg(file):
	dur = await re_encode_video(file)
	assert dur == pytest.approx(5.)

if __name__ == '__main__':
    pytest.main(['-x',__file__])