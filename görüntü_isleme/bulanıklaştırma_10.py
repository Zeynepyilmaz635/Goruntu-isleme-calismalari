# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 16:44:54 2024

@author: pc
"""

print("bulanıklaştırma_10")

import cv2
import numpy as np

img=cv2.imread('NYC.jpg')

# blurring (detayı azaltır , gürültüyü engeller)

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
ortalama bulanıklaştırma yöntemi
"""

dst2=cv2.blur(img,ksize=(3,3))
cv2.imshow("ORT_BLUR",dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Gaussian blur bulanıkşatırma
"""

dst3=cv2.GaussianBlur(img, ksize=(5,5), sigmaX=7)
cv2.imshow("gaussian_blur",dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
Median blur bulanıklaştırma
"""

dst4=cv2.medianBlur(img, ksize=3)
cv2.imshow("median_blur",dst4)
cv2.waitKey(0)
cv2.destroyAllWindows()



"""
GAUSSİAN NOISE
"""
def gaussianNoise(image):
    row,col,ch=image.shape
    mean=0
    var=0.05
    sigma=var**0.5
    
    gauss=np.random.normal(mean,sigma,(row,col,ch))
    gauss=gauss.reshape(row,col,ch)
    
    noisy=image+gauss
    return noisy
    

img=cv2.imread('NYC.jpg')

# içe aktar normalize et

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)/255

gausiianNoisyImage=gaussianNoise(img)
cv2.imshow("gaussian noisy ımage",gausiianNoisyImage)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
GAUSSİAN BLUR : noisy ları azaltmaya çalştık
"""
gb=cv2.GaussianBlur(gausiianNoisyImage, ksize=(3,3), sigmaX=7)
cv2.imshow("gaussian_blur",gb)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
Tuz karabiber görüntüsü
"""

def saltPepperNoise(image):
    row,col,cg=image.shape
    s_vs_p=0.5
    amount=0.004
    noisy=np.copy(image)
    
    # salt tuz
    num_salt=np.ceil(amount*image.size*s_vs_p)
    coords=[np.random.randint(0,i-1,int(num_salt)) for i in image.shape]
    noisy[coords]=1
    
    # siyah tuz
    num_pepper=np.ceil(amount*image.size*(1-s_vs_p))
    coords=[np.random.randint(0,i-1,int(num_pepper)) for i in image.shape]
    noisy[coords]=0   # siyah nokta
    
    return noisy
    

spImage=saltPepperNoise(img)
cv2.imshow("salt_pepper_img",spImage)
cv2.waitKey(0)
cv2.destroyAllWindows()




salt_tuz_median_blur=cv2.medianBlur(spImage.astype(np.float32), ksize=3)
cv2.imshow("salt_tuz_median_blur",salt_tuz_median_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()




































