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

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT()
#sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)

img=cv2.drawKeypoints(gray,kp)

show_img('With SIFT', img)
