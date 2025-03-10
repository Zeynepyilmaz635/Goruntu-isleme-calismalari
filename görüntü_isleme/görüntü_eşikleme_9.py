# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 16:22:16 2024

@author: pc
"""

print("görüntü_eşikleme_9")

import cv2
import matplotlib.pyplot as plt

img=cv2.imread("img1.jpg")
if img is None:
    print("Resim yüklenemedi.")
else:
    print("Resim başarıyla yüklendi.")

img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Görüntü", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# eşiklmee
_,thresh_img=cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY)

# cv2.THRESH_BINARY 60 dan yukarı olanları beyz devamını siyah yapar _BINARY_INVERSE İSE 60 dan büyük olanları siyah devamını beyaz yapar
cv2.imshow("thres img",thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()





# yuvarlamalı eşik değeri


thresh_img2=cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,8)

cv2.imshow("thres_img_2",thresh_img2)

cv2.waitKey(0)
cv2.destroyAllWindows()























