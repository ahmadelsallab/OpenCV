'''
Created on Jan 17, 2017

@author: aelsalla
'''
import cv2
import numpy as np
def show_img(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    
    

# Original image
img = cv2.imread('..\\messi5.jpg')
#img = cv2.imread('..\\j.png')

show_img('orig', img)

# Erode
kernel = np.ones((5,5),np.uint8)  
erosion = cv2.erode(img,kernel,iterations = 1)
show_img('eros_1', erosion) # White areas are highly thinned, that they are mostly disappearing

# Sharp erosion
kernel = np.ones((2,2),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
show_img('eros_2', erosion) # Better thinning (see Unicef text)


#Dilation
kernel = np.ones((5,5),np.uint8)  
dilation = cv2.dilate(img,kernel,iterations = 1)
show_img('dil_1', dilation) # Very thick white areas

# Sharp dilation
kernel = np.ones((2,2),np.uint8)  
dilation = cv2.dilate(img,kernel,iterations = 1)
show_img('dil_2', dilation)

# Add salt and pepper
image = img
row,col,ch = image.shape
s_vs_p = 0.5
amount = 0.004
out = image
num_salt = np.ceil(amount * image.size * s_vs_p)
coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
out[coords] = 1
show_img('S&P', out)
img = out

# Opening = erosion (thin) + dilation (wide)--> Remove salt
kernel = np.ones((5,5),np.uint8)  
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
show_img('open_1', opening)

# Closing = dialtion (wide) + Erosion (thin) --> Remove pepper
kernel = np.ones((5,5),np.uint8)  
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
show_img('clos_1', closing)

# Gradient = dilation - erosion
kernel = np.ones((5,5),np.uint8)  
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
show_img('grad_1', gradient)

# Close all
cv2.destroyAllWindows()