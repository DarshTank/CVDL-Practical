import cv2
import numpy as np

image = cv2.imread('samplegray.jpeg')
negative = 255 - image
cv2.imshow('Original', image)
cv2.imshow('Negative', negative)
cv2.waitKey(0)
cv2.destroyAllWindows()
