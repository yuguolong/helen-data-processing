import cv2
import numpy as np

img = cv2.imread('./png/10405146_1.jpg')
img1 = cv2.imread('./jpg/10405146_1.jpg')

w,h,_ = img.shape

for i in range(w):
    for j in range(h):
        img1[i][j][0] = img[i][j][0] * img1[i][j][0]
        img1[i][j][1] = img[i][j][1] * img1[i][j][1]
        img1[i][j][2] = img[i][j][2] * img1[i][j][2]

img1 = cv2.resize(img1,(480,640))
cv2.imshow('img',img1)
cv2.waitKey(0)