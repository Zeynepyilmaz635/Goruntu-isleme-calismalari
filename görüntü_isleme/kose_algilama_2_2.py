# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 13:58:59 2024

@author: pc
"""

print("kose_algilama_2_2")

import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("sudoku.jpg",0)

img=np.float32(img)
print(img.shape)

plt.figure() , plt.imshow(img,cmap="gray"),plt.axis("off"),plt.show()

# harriscorner detection
dst=cv2.cornerHarris(img,blockSize=2,ksize=3,k=0.04)
# blocksize komşu boyutu ksize kutucuk boyutu 

plt.figure(),plt.imshow(dst,cmap="gray"),plt.axis("off"),plt.show()

dst=cv2.dilate(dst,None)  #  dst deki tespit edilen köşeleri genşlettik
img[dst>0.2*dst.max()]=1
plt.figure(),plt.imshow(dst,cmap="gray"),plt.axis("off"),plt.show()



#  kenar algılama yöntemi shi tomsai detection

img2=cv2.imread("sudoku.jpg",0)
img2=np.float32(img2)
corners=cv2.goodFeaturesToTrack(img2,120, 0.01, 10)
corners=np.int64(corners)

for i in corners:
    x,y =i.ravel()
    cv2.circle(img2,(x,y),3,(125,125,125),cv2.FILLED)
    
plt.imshow(img2)
plt.axis("off")
plt.show()















