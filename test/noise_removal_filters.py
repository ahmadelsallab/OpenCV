'''
Created on Jan 17, 2017

@author: aelsalla
'''
import cv2
import numpy as np
def show_img(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

# Original image
img = cv2.imread('..\\messi5.jpg')

show_img(img)
# Random noise
image = img
row,col,ch= img.shape
mean = 0

gauss = np.random.normal(mean,1,(row,col,ch))
gauss = gauss.reshape(row,col,ch)
noisy = image + gauss

show_img(noisy)

# Salt an pepper image
image = img
row,col,ch = image.shape
s_vs_p = 0.5
amount = 0.004
out = image
num_salt = np.ceil(amount * image.size * s_vs_p)
coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
out[coords] = 1
show_img(out)

# Remove S&P with Blur/Avg [1111..11]
blur = cv2.blur(out,(5,5))
show_img(blur)

# With Gaussian
blur = cv2.GaussianBlur(out,(5,5),0)
show_img(blur)

# With median
median = cv2.medianBlur(out,5)
show_img(median)

# With Bi-lateral (keeping edges)
blur = cv2.bilateralFilter(out,9,75,75)
show_img(blur)

