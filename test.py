import pytest
import myffmpeg.ffprobe as probe
import myffmpeg.convert as convert
from pytest import approx


def test_duration():
    fnin = 'sunny.mp4'
    fnout = 'file_480p.mp4'

    orig_meta = probe.ffprobe(fnin)
    orig_duration = float(orig_meta['streams'][0]['duration'])

    # convert(fnin, fnout, 480)

    meta_480 = probe.ffprobe(fnout)
    duration_480 = float(meta_480['streams'][0]['duration'])

    assert orig_duration == approx(duration_480)