import cv2;
from matplotlib import pyplot 

img = cv2.imread('test.jpg',0)
pyplot.imshow(img, cmap = 'gray', interpolation = 'bicubic')
pyplot.xticks([])
pyplot.yticks([])  # to hide tick values on X and Y axis
pyplot.show()
