# import myffmpeg.ffprobe as probe
# from pytest import approx


# def test_duration():
#     # fnin = 'sunny.mp4'
#     # fnout = 'file_480p.mp4'

#     # orig_meta = probe.ffprobe(fnin)
#     # orig_duration = float(orig_meta['streams'][0]['duration'])

#     # # convert(fnin, fnout, 480)

#     # meta_480 = probe.ffprobe(fnout)
#     # duration_480 = float(meta_480['streams'][0]['duration'])

#     # assert orig_duration == approx(duration_480)

#     info_in = subprocess.check_output(['ffprobe', '-v', 'warning', '-print_format', 'json', '-show_streams',
#                                            '-show_format', 'sunny.mp4'])
#     info_in = json.loads(info_in)
#     info_out = subprocess.check_output(['ffprobe', '-v', 'warning', '-print_format', 'json', '-show_streams',
#                                             '-show_format', './file_480p.mp4'])
#     info_out = json.loads(info_out)
#     orig_duration = float(info_in['streams'][0]['duration'])
#     new_duration = float(info_out['streams'][0]['duration'])
#     assert orig_duration == new_duration


import subprocess
import json
import os
class TestClass(object):
    def test_one(self):
        while not (os.path.exists('./video/out480p.mp4')):
            pass
        info_in = subprocess.check_output(['ffprobe', '-v', 'warning', '-print_format', 'json', '-show_streams',
                                           '-show_format', 'newvideo.mp4'])  # check output
        info_in = json.loads(info_in)
        info_out = subprocess.check_output(['ffprobe', '-v', 'warning', '-print_format', 'json', '-show_streams',
                                            '-show_format', './video/out480p.mp4'])
        info_out = json.loads(info_out)
        orig_duration = float(info_in['streams'][0]['duration'])  # check if there is any difference
        new_duration = float(info_out['streams'][0]['duration'])
        assert orig_duration == new_duration

def ffprobe(patin,patout):
    info_in = subprocess.check_output(['ffprobe', '-v', 'warning','-print_format', 'json','-show_streams',
                                       '-show_format', patin])  #check output
    info_in = json.loads(info_in)   #load the info
    info_out = subprocess.check_output(['ffprobe', '-v', 'warning','-print_format', 'json','-show_streams',
                                       '-show_format', patout])
    info_out = json.loads(info_out)
    orig_duration = float(info_in['streams'][0]['duration'])  # check if there is any difference
    new_duration =  float(info_out['streams'][0]['duration'])
    if orig_duration == new_duration:
        return True
    else:
        return False