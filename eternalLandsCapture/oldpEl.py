import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
from imutils.perspective import four_point_transform
from imutils import contours
import imutils

#os.system('shutter -n -c -e --disable_systray -o elCapt.png --window=.*Joachim.*')

# Load an color image in color without alpha (for gray use 0, for alpha color use -1)
img = cv2.imread('elCapt.png',1)
height, width, _ = img.shape

imgB = cv2.imread('elCapt.png',0)

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
hip = int((818 * 100 / 866) / 100 * height)
print('origins: food(', hip, ',', wipfood, ') health(', hip, ',', wiphealth, ') load(', hip, ',', wipload, ')')
imgFood = img[hip:hip+vheight, wipfood:wipfood+vwidth]
imgHealth = img[hip:hip+vheight, wiphealth:wiphealth+vwidth]
imgLoad = img[hip:hip+vheight, wipload:wipload+vwidth]
bimgFood = imgB[hip:hip+vheight, wipfood:wipfood+vwidth]
bimgHealth = imgB[hip:hip+vheight, wiphealth:wiphealth+vwidth]
bimgLoad = imgB[hip:hip+vheight, wipload:wipload+vwidth]
#imgHarv = img[?, ?]
################

_,cimgFood = cv2.threshold(bimgFood, 75, 255, cv2.THRESH_BINARY)
_,cimgHealth = cv2.threshold(bimgHealth, 75, 255, cv2.THRESH_BINARY)
_,cimgLoad = cv2.threshold(bimgLoad, 75, 255, cv2.THRESH_BINARY)

mask = 255 * np.ones((60, 60, 3), np.uint8)
mask[18:18+13, 12:12+28] = imgFood
imgFood = cv2.resize(mask, (120, 120), interpolation = cv2.INTER_AREA)

mask = np.zeros((60, 60), np.uint8)
mask[18:18+13, 12:12+28] = cimgFood
cimgFood = cv2.resize(mask, (120, 120), interpolation = cv2.INTER_AREA)

mask = 255 * np.ones((60, 60, 3), np.uint8)
mask[18:18+13, 12:12+28] = imgHealth
imgHealth = cv2.resize(mask, (120, 120), interpolation = cv2.INTER_AREA)

mask = np.zeros((60, 60), np.uint8)
mask[18:18+13, 12:12+28] = cimgHealth
cimgHealth = cv2.resize(mask, (120, 120), interpolation = cv2.INTER_AREA)

mask = 255 * np.ones((60, 60, 3), np.uint8)
mask[18:18+13, 12:12+28] = imgLoad
imgLoad = cv2.resize(mask, (120, 120), interpolation = cv2.INTER_AREA)

mask = 255 * np.zeros((60, 60), np.uint8)
mask[18:18+13, 12:12+28] = cimgLoad
cimgLoad = cv2.resize(mask, (120, 120), interpolation = cv2.INTER_AREA)

_, contours, _ = cv2.findContours(cimgLoad, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imgLoad, contours, -1, (0,255,0), 1)

#cv2.imshow('image',imgHarv)
titles = ['food', 'health', 'load']
images = [imgFood, imgHealth, imgLoad]
for i in range(3):
    plt.subplot(3,1,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

#cv2.imwrite('elHarvesting.png',imgHarv)
cv2.imwrite('elHealth.png',imgHealth)
cv2.imwrite('elFood.png',imgFood)
cv2.imwrite('elLoad.png',imgLoad)

#k = cv2.waitKey(0) & 0xFF
#if k == 27:         # wait for ESC key to exit
#    cv2.destroyAllWindows()
#elif k == ord('s'): # wait for 's' key to save and exit
#    #cv2.imwrite('elHarvesting.png',imgHarv)
#    cv2.imwrite('elHealth.png',imgHealth)
#    cv2.imwrite('elFood.png',imgFood)
#    cv2.imwrite('elLoad.png',imgLoad)
#    cv2.destroyAllWindows()

#img = cv.medianBlur(img,5)
#ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
#th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
#            cv.THRESH_BINARY,11,2)
#th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
#            cv.THRESH_BINARY,11,2)
#titles = ['Original Image', 'Global Thresholding (v = 127)',
#            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
#images = [img, th1, th2, th3]
#for i in xrange(4):
#    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])
#plt.show()

