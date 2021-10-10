# encoding: utf-8
"""
@author:  sunfine
@contact: 275631245@qq.com
"""
import cv2
from glob import glob

video_list = glob('/mnt/ssd1/studentData/linyinglun/lyl练习用/kaggle_vip/kaggle_helmet/data/test/*mp4')
for video in video_list:
      # print(video)
  vc=cv2.VideoCapture(video)
  c=1
  if vc.isOpened():
    rval,frame=vc.read()
  else:
    rval=False

  timeF = 1
  while rval:
    rval,frame=vc.read()
    if c % timeF == 0:
      cv2.imwrite(r'/mnt/ssd1/studentData/linyinglun/lyl练习用/kaggle_vip/kaggle_helmet/data/test_video_to_jpg/'+video.split('/')[-1].rstrip('.mp4')+'_'+str(c)+'.jpg',frame)
    c=c+1
    cv2.waitKey(1)
  vc.release()