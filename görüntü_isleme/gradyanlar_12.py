# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 20:51:00 2024

@author: pc
"""

print("gradyanlar_12")
import cv2
img=cv2.imread("sudoku.jpg",0)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#  x gradtyan

sobelx=cv2.Sobel(img,ddepth=cv2.CV_16S,dx=1,dy=0,ksize=5)
cv2.imshow("x gradyan",sobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()

sobely=cv2.Sobel(img,ddepth=cv2.CV_16S,dx=0,dy=1,ksize=5)
cv2.imshow("y gradyan",sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()

#  laplacian gradyan
laplacian=cv2.Laplacian(img,ddepth=cv2.CV_16S)
cv2.imshow("x ve y" , laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()