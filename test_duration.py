from pytest import approx
import subprocess


def test_duration():
    
    #define all test files in the list
    fnin = './test.mp4'
    
    fnout_480 = './file_480p.mp4'
    
    fnout_720 = './file_720p.mp4'

    # orig_meta = probe.ffprobe(fnin)
    # orig_duration = float(orig_meta['streams'][0]['duration'])

    # # convert(fnin, fnout, 480)

    # meta_480 = probe.ffprobe(fnout)
    # duration_480 = float(meta_480['streams'][0]['duration'])

    #assert orig_duration == approx(duration_480)

    info_in = subprocess.call(['ffprobe', '-v', 
                                'warning', '-print_format',
                                 'json', '-show_streams', 
                                 '-show_format', fnin])
    info_out_480 = subprocess.call(['ffprobe', '-v', 
                                'warning', '-print_format',
                                 'json', '-show_streams', 
                                 '-show_format', fnout_480])
    info_out_720 = subprocess.call(['ffprobe', '-v', 
                                'warning', '-print_format',
                                 'json', '-show_streams', 
                                 '-show_format', fnout_720])

    assert info_in == approx(info_out_480)
    assert info_in == approx(info_out_720)

if __name__ == '__main__':
    test_duration()