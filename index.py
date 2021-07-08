import cv2
import numpy as np
from imutils import resize
from pygame import mixer 
mixer.init()
cap=cv2.VideoCapture(0)
a=0
b=0
alpha=0.5
while True:
      
      _, frame= cap.read()
      hsv_frame= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
      bassim=cv2.imread("bass.jpg")
      bim=resize(bassim,width=200,height=200)
      cymbalsim=cv2.imread("cymbals.jpg")
      sim=resize(cymbalsim,width=200,height=200)
      low_black = np.array([0,0,0])
      high_black = np.array([353,352 ,100 ])
      black_mask = cv2.inRange(hsv_frame  ,  low_black,  high_black)
      black = cv2.bitwise_and(frame , frame , mask=black_mask)
      bbcheck=black[260:460,25:225]
      sbcheck=black[260:460,410:610]
      added_image1 = cv2.addWeighted(frame[260:460,25:225,:],alpha,bim[0:200,0:200,:],1-alpha,0)
      added_image2 = cv2.addWeighted(frame[260:460,410:610,:],alpha,sim[0:200,0:200,:],1-alpha,0)
      frame[260:460,25:225] = added_image1
      frame[260:460,410:610] = added_image2
      cv2.imshow('Virtual Drum',frame)
      if np.average(bbcheck)>=10 and a==0 and b==0:
          mixer.music.load('bass.ogg')
          mixer.music.play()
          a=1
      if np.average(bbcheck)<10 and a==1:
          mixer.music.stop()
          a=0 
      if np.average(sbcheck)>=10 and b==0 and a==0:
          mixer.music.load('cymbal.ogg')
          mixer.music.play()
          b=1
      if np.average(sbcheck)<10 and b==1:
          mixer.music.stop()
          b=0         
      key= cv2.waitKey(1)
      if key == ord('q'):
        break