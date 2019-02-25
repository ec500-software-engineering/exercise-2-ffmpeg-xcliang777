import os
import threading
import queue
import subprocess
import duration


def re_encode_video(file):
	try:
		subprocess.call(['ffmpeg', '-i', file, '-r', '30', '-b:v', '2M', '-s', 'hd720', 'file_720p.mp4'])
		print('processing' + file + 'to 720P DONE')
	except Exception as e:
		print(e)

	try:
		subprocess.call(['ffmpeg', '-i', file, '-r', '30', '-b:v', '2M', '-s', 'hd480', 'file_480p.mp4'])
		print('processing' + file + 'to 480P DONE')
	except Exception as e:
		print(e)

	# try:
	# 	os.system('ffmpeg -i ' + file + ' -r 30 -b 2M -loglevel quiet -s 1280x720 ' + file + '_720.mp4')
	# 	print('processing' + file + 'to 720P DONE')
	# except Exception as e:
	# 	print(e)

	# try:
	# 	os.system('ffmpeg -i ' + file + ' -r 30 -b 1M -loglevel quiet -s 720x480 ' + file + '_480.mp4')
	# 	print('processing' + file + 'to 480P DONE')
	# except Exception as e:
	# 	print(e)


def main():
	q = queue.Queue()
	thread_list = []
	t = 0

	'''Serrch all mp4/mov files in the directory'''
	try:
		
		for file in os.listdir("./"):
			if file.endswith('.mp4'):
				t = t + 1
				#print(file)
				q.put(file)
				thread_list.append(threading.Thread(target = re_encode_video, args = (file, )))
				duration.test_duration(file)

	except Exception as e:
		print(e)

	print(str(t) + ' files in the process')

	for thread in thread_list:
		thread.start()

	#print('Your videos are already here')


if __name__ == '__main__':
    main()