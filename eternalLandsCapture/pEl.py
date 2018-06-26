import numpy as np
import cv2
import os

os.system('shutter -n -c -e --disable_systray -o elCapt.png --window=.*Joachim.*')

# Load an color image in color without alpha (for bw use 0, for alpha color use -1)
img = cv2.imread('elCapt.png',1)
height, width, _ = img.shape
harvHeight = int(0.97 * height)
harvWidth = int(0.9 * width)
harvSize = int(0.033 * height)

imgB = cv2.imread('elCapt.png',1)
healthWidth = int(0.188 * width)
foodWidth = int(0.1 * width)
loadWidth = int(0.28 * width)
hflHeight = int(0.93 * height)
hflSize = int(0.033 * height)

#imgHarv = img[840:840+36, 1388:1388+28]
#imgHarv = img[harvHeight:harvHeight+28, harvWidth:harvWidth+28]
imgHarv = img[harvHeight:harvHeight+harvSize, harvWidth:harvWidth+harvSize]
imgHealth = imgB[hflHeight:hflHeight+hflSize, healthWidth:healthWidth+hflSize]
imgFood = imgB[hflHeight:hflHeight+hflSize, foodWidth:foodWidth+hflSize]
imgLoad = imgB[hflHeight:hflHeight+hflSize, loadWidth:loadWidth+hflSize]
cv2.imshow('image',imgHarv)
cv2.imshow('image1',imgHealth)
cv2.imshow('image2',imgFood)
cv2.imshow('image3',imgLoad)
k = cv2.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('elHarvesting.png',imgHarv)
    cv2.imwrite('elHealth.png',imgHealth)
    cv2.imwrite('elFood.png',imgFood)
    cv2.imwrite('elLoad.png',imgLoad)
    cv2.destroyAllWindows()
