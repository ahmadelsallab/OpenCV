'''
Created on Jan 17, 2017

@author: aelsalla
'''
import cv2

def show_img(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)

img = cv2.imread('..\\messi5.jpg')
show_img('img', img)
lower_res = cv2.pyrDown(img)
show_img('low', lower_res)
lower_res = cv2.pyrDown(lower_res)
show_img('low', lower_res)
upper_res = cv2.pyrUp(lower_res)
show_img('up', upper_res)
upper_res = cv2.pyrUp(upper_res)
show_img('up', upper_res) # cannot recover orig image due to lost info in sub sampling
upper_res = cv2.pyrUp(upper_res)
show_img('up', upper_res)# More and more corrupted image (not blurred)


'''
import cv2
import numpy as np,sys

A = cv2.imread('..\\messi5.jpg')
B = cv2.imread('..\\messi5.jpg')
#B = cv2.imread('..\\j.png')
# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in xrange(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in xrange(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols/2], lb[:,cols/2:]))
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in xrange(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half
real = np.hstack((A[:,:cols/2],B[:,cols/2:]))

cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real)
'''