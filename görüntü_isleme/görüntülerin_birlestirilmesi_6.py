# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 20:03:22 2024

@author: pc
"""

print("görüntülerin_birlestirilmesi_6")

import cv2
import numpy as np
img=cv2.imread("lenna.png")
cv2.imshow("orjinal",img)

if cv2.waitKey(0) & 0xFF ==ord('s'):
    cv2.destroyAllWindows()
    
    
hor=np.hstack((img,img))
cv2.imshow("horizontal",hor)

if cv2.waitKey(0) &0xFF ==ord('q'):
    cv2.destroyAllWindows()
    
ver=np.vstack((img,img))
cv2.imshow("vertical", ver)

if cv2.waitKey(0) &0xFF==ord('k'):
    cv2.destroyAllWindows()