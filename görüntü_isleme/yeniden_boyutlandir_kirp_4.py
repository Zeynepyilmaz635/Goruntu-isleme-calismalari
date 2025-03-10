# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:36:17 2024

@author: pc
"""

print("yeniden_boyutlandir_kirp")

import cv2

img=cv2.imread("lenna.png")
print("resim boyutu : " , img.shape)

cv2.imshow("lenna_org", img)

if cv2.waitKey(0) & 0xFF ==ord('q'):
    cv2.destroyAllWindows()
    


# resized
imgResized=cv2.resize(img,(800,800))
print("resized image : " , imgResized.shape)



cv2.imshow("boyutlu_img", imgResized)
if cv2.waitKey(0) & 0XFF == ord('s'):
    cv2.destroyAllWindows()
    
    
# kırp 
imgCropped = img[:200,0:300] # yükseklik , genişlik 
cv2.imshow("kırpık resim",imgCropped)
if cv2.waitKey(0) & 0xFF ==ord('q'):
    cv2.destroyAllWindows()






