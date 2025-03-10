# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:35:54 2024

@author: pc
"""

import cv2
import numpy as np
from collections import deque

# nesne merkezini depolayacak veri tipi
buffer_size = 16
pts = deque(maxlen=buffer_size)

# mavi renk aralığı HSV formatında
blueLower = (84, 98, 0)
blueUpper = (179, 255, 255)

# capture
cap = cv2.VideoCapture(0)
cap.set(3, 960)  # genişlik görüntünün
cap.set(4, 480)  # yükseklik

while True:
    success, imgOriginal = cap.read()
    if success:
        # blur
        blurred = cv2.GaussianBlur(imgOriginal, (11, 11), 0)

        # hsv
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        cv2.imshow("HSV image", hsv)

        # mavi için maske oluştur
        mask = cv2.inRange(hsv, blueLower, blueUpper)
        cv2.imshow("mask image", mask)

        # erozyon ve genişleme ile mavi haricindeki şeylerden gürültüleri arındırıyoruz
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cv2.imshow("mask + erozyon + genişleme", mask)

        # kontür algılama
        contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        center = None  # nesnemizin merkezi
        if len(contours) > 0:
            # en büyük kontürü al
            c = max(contours, key=cv2.contourArea)
            # dikdörtgene çevir kontürleri
            rect = cv2.minAreaRect(c)
            ((x, y), (width, height), rotation) = rect
            s = "x : {} , y : {} , width : {} , height : {} , rotation : {}".format(
                np.round(x), np.round(y), np.round(width), np.round(height), np.round(rotation)
            )
            print(s)

            # kutucuk nesnenin etrafını kaplamak için
            box = cv2.boxPoints(rect)
            box = np.int64(box)

            # moment: görüntünün yarı çapı vs görüntünün merkezi
            M = cv2.moments(c)
            if M["m00"] != 0:
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            # kontürü çizdirme: sarı
            cv2.drawContours(imgOriginal, [box], 0, (0, 255, 255), 2)
            # merkeze bir tane nokta çizelim: pembe
            if center is not None:
                cv2.circle(imgOriginal, center, 5, (255, 0, 255), -1)

            # bilgileri ekrana yazdıralım
            cv2.putText(imgOriginal, s, (25, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        # NESNE TAKİBİ YAPTIK
        pts.appendleft(center)
        for i in range(1, len(pts)):
            if pts[i - 1] is None or pts[i] is None:
                continue
            cv2.line(imgOriginal, pts[i - 1], pts[i], (0, 255, 0), 3)

        cv2.imshow("orijinal tespit", imgOriginal)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

cap.release()s

        
        
        
        
        
        
        
        
        
        
        
        
        

