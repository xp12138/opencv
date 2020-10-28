# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:54:15 2020

@author: sharpen
"""


import cv2 as cv
from matplotlib import pyplot as plt

src = cv.imread(r'C:\Users\Administrator\Desktop\slight.png')
ret,dst1 = cv.threshold(src,127,255,cv.THRESH_BINARY)
ret,dst2 = cv.threshold(src,127,255,cv.THRESH_BINARY_INV)
ret,dst3 = cv.threshold(src,127,255,cv.THRESH_TRUNC)
ret,dst4 = cv.threshold(src,127,255,cv.THRESH_TOZERO)
ret,dst5 = cv.threshold(src,127,255,cv.THRESH_TOZERO_INV)
titles = ['original','BINARY','BINARY_INV','TRUNC','THRESH_TOZERO','THRESH_TOZERO_INV']
imgs = [src,dst1,dst2,dst3,dst4,dst5]
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(imgs[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()