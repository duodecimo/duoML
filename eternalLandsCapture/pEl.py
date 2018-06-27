import numpy as np
import cv2
import os

os.system('shutter -n -c -e --disable_systray -o elCapt.png --window=.*Joachim.*')

# Load an color image in color without alpha (for gray use 0, for alpha color use -1)
img = cv2.imread('elCapt.png',1)
height, width, _ = img.shape

imgB = cv2.imread('elCapt.png',1)

################
# orinal size 1545 x 866
# percentages
vheight = int((13 * 100 / 866) / 100  * height)
vwidth = int((28 * 100 / 1545) / 100 * width)
print('height: ', vheight, ' width: ', vwidth)
# origins
wipfood = int((148 * 100 / 1545) / 100 * width)
wiphealth = int((289 * 100 / 1545) / 100 * width)
wipload = int((430 * 100 / 1545) / 100 * width)
hip = int((816 * 100 / 866) / 100 * height)
print('origins: food(', hip, ',', wipfood, ') health(', hip, ',', wiphealth, ') load(', hip, ',', wipload, ')')
imgFood = imgB[hip:hip+vheight, wipfood:wipfood+vwidth]
imgHealth = imgB[hip:hip+vheight, wiphealth:wiphealth+vwidth]
imgLoad = imgB[hip:hip+vheight, wipload:wipload+vwidth]
#imgHarv = img[?, ?]
################

#cv2.imshow('image',imgHarv)
cv2.imshow('food',imgFood)
cv2.imshow('health',imgHealth)
cv2.imshow('load',imgLoad)
k = cv2.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    #cv2.imwrite('elHarvesting.png',imgHarv)
    cv2.imwrite('elHealth.png',imgHealth)
    cv2.imwrite('elFood.png',imgFood)
    cv2.imwrite('elLoad.png',imgLoad)
    cv2.destroyAllWindows()
