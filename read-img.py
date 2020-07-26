import cv2
# import numpy as np
# np.set_printoptions(threshold=np.inf)

img = cv2.imread('labels\\2908549_1\\2908549_1_lbl07.png')
img1 = cv2.imread('./jpg/2908549_1.jpg')

# img = img*img1
img = cv2.addWeighted(img,0.6,img1,0.4,0)
cv2.imwrite('./10697993_1_lbl09.png',img)
# img = np.array(img)

# img = img.tolist()
# nums = set(str(img))
# print(img)
# a = [i for i in range(256)]
# w,h,_ = img.shape
#
# for i in range(w):
#     for j in range(h):
#         print(img[i][j])