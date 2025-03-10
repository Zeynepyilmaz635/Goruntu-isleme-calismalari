# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:16:12 2024

@author: pc
"""

print("resim_ice_aktarma_1")

import cv2

#  içe aktarma
img=cv2.imread("messi5.jpg",0)

#  görsellştir
cv2.imshow("ilk resim",img)


k=cv2.waitKey(0) &0xFF
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite("messi_gray.png",img)
    cv2.destroyAllWindows()


