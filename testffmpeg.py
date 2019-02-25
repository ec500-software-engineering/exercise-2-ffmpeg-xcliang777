import pytest
import main

@pytest.mark.asyncio
async def test_ffmpeg():
	dur = await main.main()
	assert dur == pytest.approx(5.)

if __name__ == '__main__':
    pytest.main(['-x',__file__])