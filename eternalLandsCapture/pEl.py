import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

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
imgFood = imgB[hip:hip+vheight, wipfood:wipfood+vwidth]
imgHealth = imgB[hip:hip+vheight, wiphealth:wiphealth+vwidth]
imgLoad = imgB[hip:hip+vheight, wipload:wipload+vwidth]
#imgHarv = img[?, ?]
################

ret,imgFood = cv2.threshold(imgFood, 75, 255, cv2.THRESH_BINARY_INV)
ret,imgHealth = cv2.threshold(imgHealth, 75, 255, cv2.THRESH_BINARY_INV)
ret,imgLoad = cv2.threshold(imgLoad, 75, 255, cv2.THRESH_BINARY_INV)

mask = 255 * np.ones((60, 60), np.uint8)
mask[18:18+13, 12:12+28] = imgFood
imgFood = cv2.resize(mask, (1200, 1200), interpolation = cv2.INTER_AREA)

mask = 255 * np.ones((60, 60), np.uint8)
mask[18:18+13, 12:12+28] = imgHealth
imgHealth = cv2.resize(mask, (1200, 1200), interpolation = cv2.INTER_AREA)

mask = 255 * np.ones((60, 60), np.uint8)
mask[18:18+13, 12:12+28] = imgLoad
imgLoad = cv2.resize(mask, (1200, 1200), interpolation = cv2.INTER_AREA)

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


# find contours in the thresholded image, then initialize the
# digit contours lists
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
digitCnts = []
 
# loop over the digit area candidates
for c in cnts:
# compute the bounding box of the contour
(x, y, w, h) = cv2.boundingRect(c)
 
# if the contour is sufficiently large, it must be a digit
if w >= 15 and (h >= 30 and h <= 40):
digitCnts.append(c)


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

