# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:51:35 2024

@author: pc
"""

print("sekiller_metin_5")

import cv2
import numpy as np

# resim oluştur

img=np.zeros((512,512,3),np.uint8) # siyah bir resim
print(img.shape)



# çizgi = line
cv2.line(img,(0,0),(512,512),(0,255,0),3) 
# resim , baş nok , bitiş nok , renk ,kalınlık

# dikdörtgen

cv2.rectangle(img,(0,0),(256,256),(255,0,0) , cv2.FILLED)
# resim , baş nok , bitiş nok , renk  , içi dolu boş kararı


# çember
# resim ,merkez , yarıçap,renk 
cv2.circle(img,(300,300),45,(0,0,255),cv2.FILLED)

#metin
# resim ,yazı ,yazının başlangıç nok , font , kalınlığı , renk 
cv2.putText(img,"resim yazısı " , (350,350),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255))





cv2.imshow("siyah",img)
if cv2.waitKey(0) & 0xFF ==ord('q'):
    cv2.destroyAllWindows()


