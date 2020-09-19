#!/usr/bin/env python

import os
import subprocess
import time
from datetime import datetime

try:
	date_time = datetime.now().strftime('%m-%d-%Y-%H-%M-%S')
	output_file = '{0}{1}'.format(date_time, '.mkv')
	output_file = os.path.join('/home/alex/webcam', output_file)

	devnull = open(os.devnull, 'w')
	recorder = subprocess.Popen(
	    ['ffmpeg', '-f', 'v4l2', '-framerate', '25', '-video_size', '320x240', '-i', '/dev/video0', output_file],
	    stdout=devnull,
	    stderr=devnull,
	)

	while True:
		for i in range(1, 4):
			print('   ', end='\r')
			print('.' * i, end='\r')
			time.sleep(1)

except (EOFError, KeyboardInterrupt):
	print('Aborted')
finally:
	recorder.terminate()
	devnull.close()
