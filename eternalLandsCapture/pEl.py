import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
from imutils.perspective import four_point_transform
from imutils import contours
import imutils

def transform(img):
  # resize
  img = cv2.resize(img, None, fx=3, fy=3, interpolation = cv2.INTER_LINEAR)
  # convert to gray scale
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # apply gaussian blur
  #img = cv2.GaussianBlur(img, (5, 5), 0)
  # threshold to black with white background
  _, img = cv2.threshold(img, 90, 255, cv2.THRESH_BINARY_INV)
  # expand the background
  ht, wh = img.shape
  mwh = int(wh/2)
  mask = 255 * np.ones((ht*3, wh*2), np.uint8)
  mask[ht*2:ht*2+ht, mwh:mwh+wh] = img
  img = mask
  return img

#os.system('shutter -n -c -e --disable_systray -o elCapt.png --window=.*Joachim.*')

# Load an color image in color without alpha (for gray use 0, for alpha color use -1)
img = cv2.imread('elCapt.png',1)
height, width, _ = img.shape


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
hip = int((817 * 100 / 866) / 100 * height)
#print('origins: food(', hip, ',', wipfood, ') health(', hip, ',', wiphealth, ') load(', hip, ',', wipload, ')')
imgFood = img[hip:hip+vheight, wipfood:wipfood+vwidth]
imgHealth = img[hip:hip+vheight, wiphealth:wiphealth+vwidth]
imgLoad = img[hip:hip+vheight, wipload:wipload+vwidth]
#imgHarv = img[?, ?]
################

imgFood = transform(imgFood)
imgHealth = transform(imgHealth)
imgLoad = transform(imgLoad)

#cv2.imwrite('elHarvesting.png',imgHarv)
cv2.imwrite('elHealth.png',imgHealth)
cv2.imwrite('elFood.png',imgFood)
cv2.imwrite('elLoad.png',imgLoad)

titles = ['food', 'health', 'load']
images = [imgFood, imgHealth, imgLoad]
for i in range(3):
    plt.subplot(3,1,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


