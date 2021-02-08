import cv2 as cv
import numpy as np 

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Point the image a certain color
'''
blank[:] = 255,0,255
cv.imshow('Colour', blank)
'''
blank[200:300, 400:500] = 255,255,0
cv.imshow('Colour', blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness = -1)
cv.imshow('Rectangle', blank)

# 3.Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness = 3)
cv.imshow('Circle', blank)

#4.Draw a line
cv.line(blank, (0,0), blank(blank.shape[1]//2, blank.shape[0]//))
cv.waitKey(0)