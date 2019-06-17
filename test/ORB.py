'''
Created on Jan 19, 2017

@author: aelsalla
'''

import cv2
import numpy as np


def show_img(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)

img = cv2.imread('..\\messi5.jpg')
show_img('orig', img)


# Initiate STAR detector
orb = cv2.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img,None) 

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
img2=img
#cv2.drawKeypoints(img,kp,color=(0,255,0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, outImage=img2)
cv2.drawKeypoints(img,kp,color=(0,255,0), flags=0, outImage=img2)
#plt.imshow(img2),plt.show()
show_img('ORB', img2)