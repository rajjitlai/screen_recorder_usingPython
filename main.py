# pip install PILLOW and then import ImageGrab
from PIL import ImageGrab
# pip install win32api and then import GetSystemMetrics
from win32api import GetSystemMetrics
# pip install cv2 and then import cv2
import cv2
# import the built in modules
import numpy as nV
import datetime

print('Created by Rajjit Laishram'[::1])

vidWidth = GetSystemMetrics(0)
vidHeight = GetSystemMetrics(1)

file_time_format = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
saved_file = f'{file_time_format}.mp4'
fileName = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
recorded_video = cv2.VideoWriter(saved_file, fileName, 30.0, (vidWidth, vidHeight))

for_webCam = cv2.VideoCapture(0)

while True:
          vid = ImageGrab.grab(bbox=(0,0, vidWidth, vidHeight))
          vid_nV = nV.array(vid)
          vid_res = cv2.cvtColor(vid_nV, cv2.COLOR_BGR2RGB)
          _, wC_frame = for_webCam.read()
          wC_height, wC_width, _ = wC_frame.shape
          vid_res[0:wC_height, 0: wC_width, :] = wC_frame[0: wC_height, 0:wC_width, :]
          
          cv2.imshow('RJs Screen Recorder', vid_res)
          # cv2.imshow('RJs WebCam Recorder', wC_frame)
          
          recorded_video.write(vid_res)
          
          if cv2.waitKey(10) == ord('x'):
                    break
          