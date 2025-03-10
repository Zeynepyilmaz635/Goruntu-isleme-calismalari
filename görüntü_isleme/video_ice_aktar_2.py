# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:24:17 2024

@author: pc
"""

print("video_ice_aktar_2")

import cv2
import time

# video ismi
video_name="MOT17-04-DPM.mp4"

# video içe aktar : capture , cap
cap=cv2.VideoCapture(video_name)

print("genişlik : " ,cap.get(3))
print("yükseklik : " ,cap.get(4))

if cap.isOpened()== False:
    print("hata")
    
while True:
    ret,frame=cap.read()
    if ret==True:
        time.sleep(0.01) #uyarı : kullanmzsak çok hızlı akar
    
        cv2.imshow("video",frame)
    else : break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
    
cap.release() # video yakalamayı bırk
cv2.destroyAllWindows()
     
    