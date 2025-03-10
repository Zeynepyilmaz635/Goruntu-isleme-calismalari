# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 20:13:48 2024

@author: pc
"""

print("persfektif_carpitma_7")

import cv2
import numpy as np

img=cv2.imread("kart.png")
cv2.imshow("orjinal",img)

if cv2.waitKey(0) &0xFF ==ord('q'):
    cv2.destroyAllWindows()
    
width=400
height=500

#anlık resmin köşe koordinatları
pts1=np.float32([[230,1],[1,472],[540,150],[338,617]])

pts2=np.float32([[0,0],[0,height],[width,0],[width,height]])

matrix=cv2.getPerspectiveTransform(pts1, pts2)

print(matrix)

# nihai dönüştürülmş resim
img2=cv2.warpPerspective(img, matrix, (width,height))

cv2.imshow("nihai resim", img2)

if cv2.waitKey(0) & 0xFF==ord('s'):
    cv2.destroyAllWindows()