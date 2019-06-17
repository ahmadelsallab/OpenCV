'''
Created on Jan 17, 2017

@author: aelsalla
'''

import cv2
import numpy as np

def show_img(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)

#im = cv2.imread('..\\messi5.jpg')
im = cv2.imread('..\\scan_sample_0.png')
#show_img('orig', im)
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#show_img('gray', imgray)
ret,thresh = cv2.threshold(imgray,127,255,0)
#show_img('thresh', thresh)

image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(im, contours, -1, (0,255,0), 3)
show_img('contours+image', img)

'''
# Thinning = Dilation
kernel = np.ones((5,5),np.uint8)  
dilation = cv2.dilate(img,kernel,iterations = 1)
show_img('dil_1', dilation) # Very thick white areas
'''
'''
# DBSCan clustering
from sklearn.cluster import DBSCAN

from sklearn.datasets.samples_generator import make_blobs
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                            random_state=0)
from sklearn.preprocessing import StandardScaler
X = StandardScaler().fit_transform(X)


db = DBSCAN(eps=0.3, min_samples=10).fit(contours)
'''

# Moments: Image moments help you to calculate some features like center of mass of the object, area of the object etc. Check out the wikipedia page on Image Moments
'''
im = cv2.imread('..\\scan_sample_0.png')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
'''
cnt = contours[5]
M = cv2.moments(cnt)
print M
area = cv2.contourArea(cnt)
print area 

# Contour approx.: Douglas-Peuker
epsilon = 0.01*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
#pts = approx.reshape((-1,1,2))
pts = approx
img = cv2.polylines(img,[pts],True,(0,255,255))
show_img('approx_contour', img)

# Convex hull
hull = cv2.convexHull(cnt)
pts = hull
img = cv2.polylines(img,[pts],True,(0,255,255))
show_img('hull', img)

# Bounding rectangle
# Straight:
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
show_img('straight_BB', img)

# Min area
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
im = cv2.drawContours(im,[box],0,(0,0,255),2)
show_img('min_Area_BB', im)

# Min enclosing area circle
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
im = cv2.circle(img,center,radius,(0,255,0),2)
show_img('min_Circle_Area_BB', im)