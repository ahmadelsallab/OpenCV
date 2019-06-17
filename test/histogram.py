'''
Created on Jan 18, 2017

@author: aelsalla
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

def show_img(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)

img = cv2.imread('..\\messi5.jpg')



show_img('CLAHE', cl1)

#im = cv2.imread('..\\scan_sample_0.png')
show_img('orig_image', img)

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()


# Equalize
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img]
show_img('Equalize', img2)

hist,bins = np.histogram(img2.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

# Equalize with opencv
'''
img = cv2.imread('..\\messi5.jpg')
equ = cv2.equalizeHist(img)

show_img('Equalize opencv', equ)

hist,bins = np.histogram(equ.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

'''
'''
# CLAHE:

import numpy as np
import cv2

img = cv2.imread('..\\messi5.jpg')

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

show_img('CLAHE', cl1)

'''
