import cv2
import numpy as np
from imutils import paths
from numba import jit
from time import time
# import concurrent.futures
from multiprocessing import Pool

@jit(nopython=True)
def save(img, label, w, h,j):
    for k in range(w):
        for z in range(h):
            if img[k][z] > 100:
                label[k][z] = j
    return label

def data(imagePaths):
    label_list = [0,1,2,2,3,3,4,5,6,5]
    true_image = cv2.imread(imagePaths)
    w,h,c = true_image.shape
    label = np.zeros((w,h))

    file = imagePaths.split('/')[-1].split('.')[0]
    for j in range(1,10):
        path = './labels/{}/{}_lbl0{}.png'.format(file,file,j)
        img = cv2.imread(path,0)
        label = save(img,label,w,h,label_list[j])
    cv2.imwrite('./png/{}.jpg'.format(file),label)

if __name__ == "__main__":
    start = time()
    imagePaths = list(paths.list_images('./jpg/'))
    # p = concurrent.futures.ProcessPoolExecutor()
    pool = Pool(4)
    pool.map(data, imagePaths)
    pool.close()
    pool.join()
    # data(imagePaths)
    print(time()-start)
#普通
#14.215826034545898s

#线程
#0.31319689750671387


#原始程序
# def data(imagePaths):
#     for i in imagePaths:
#         if 'jpg' in i:
#             true_image = cv2.imread(i)
#             w,h,c = true_image.shape
#             label = np.zeros((w,h))
#
#             file = i.split('/')[-1].split('.')[0]
#             for j in range(1,10):
#                 path = './labels/{}/{}_lbl0{}.png'.format(file,file,j)
#                 img = cv2.imread(path,0)
#                 label = save(img,label,w,h,j)
#
#             cv2.imwrite('./png/{}.jpg'.format(file),label)
# start = time()
# imagePaths = list(paths.list_images('./jpg1/'))
# data(imagePaths)
# print(time()-start)

#63.68670201301575s
#多进程
#27.687963724136353s