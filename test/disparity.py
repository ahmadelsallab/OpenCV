'''
Created on Jan 23, 2017

@author: aelsalla
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt
def show_img(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    
imgL = cv2.imread('..\\myleft.jpg',0)
imgR = cv2.imread('..\\myright.jpg',0)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
#stereo = cv2.StereoBM_create(cv2.STEREO_BM_BASIC_PRESET,ndisparities=16, SADWindowSize=15)
disparity = stereo.compute(imgL,imgR)
show_img('left', imgL)
show_img('right', imgR)
#show_img('disparity', disparity)
plt.imshow(disparity,'gray')
plt.show()

