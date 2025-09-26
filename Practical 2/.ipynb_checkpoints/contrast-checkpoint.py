import cv2
import numpy as np

image = cv2.imread('samplegray.jpeg')
alpha = 1.5
beta = 3
adjusted = np.clip(alpha * image + beta, 0, 255).astype(np.uint8)
cv2.imshow('Original', image)
cv2.imshow('Contrast', adjusted)
cv2.waitKey(0)
cv2.destroyAllWindows()
