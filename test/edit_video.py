'''
Created on Jan 22, 2017

@author: aelsalla
'''

import cv2
import numpy as np
def show_img(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    
    



#cap = cv2.VideoCapture('..\\DeepTracking_RNN.avi')
#cap = cv2.VideoCapture('..\\ScaLa.avi ')
cap = cv2.VideoCapture('C:\\Valeo\\DAS\\Presentations\\DL\\Demos\\LaneKeeping_EvoNeuralNets and CarMaker.avi')
frame_cnt = 0
#times = [['start', 20, 'end', 30],['start', 55, 'end', 77],['start', 220, 'end', 240]]
times =  [(20, 30), (55,77), (220,240)]
time_idx = 0
fps = 10
ret,frame = cap.read()
while(frame != None):
    #ret,frame = cap.read()

    '''
    cv2.imshow('frame',frame)
    k = cv2.waitKey(0) & 0xff
    if k == 27:
        break
    '''
    frame_cnt += 1
    
    if (frame_cnt == times[time_idx][0] * fps):
        show_img('frame', frame)    
        time_idx += 1
    
    ret,frame = cap.read()
print(frame_cnt)
cv2.destroyAllWindows()
cap.release()