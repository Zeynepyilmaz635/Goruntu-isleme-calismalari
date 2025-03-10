
import cv2

import numpy as np

# resmi içe aktar
img = cv2.imread("london.jpg", 0)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

edges = cv2.Canny(image = img, threshold1 = 0, threshold2 = 255)  #  kenarları algılama fonk
cv2.imshow("edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

med_val = np.median(img) 
print(med_val)

low = int(max(0, (1 - 0.33)*med_val)) #  alt threshold değerini aldk
high = int(min(255, (1 + 0.33)*med_val)) #  üst treshold değerini aldk

print(low)
print(high)

edges = cv2.Canny(image = img, threshold1 = low, threshold2 = high)
cv2.imshow("edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# blur
blurred_img = cv2.blur(img, ksize = (5,5)) #  blurring yaptık ki resimdemesela denizdekileri ayrıntı kenar almasın diye blurring uyguladk
cv2.imshow("blurred_img", blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

med_val = np.median(blurred_img)
print(med_val)

low = int(max(0, (1 - 0.33)*med_val))
high = int(min(255, (1 + 0.33)*med_val))

print(low)
print(high)

edges = cv2.Canny(image = blurred_img, threshold1 = low, threshold2 = high) #  blurrimg uygulanan resimde kenar tespiti yaptk
cv2.imshow("edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()



















