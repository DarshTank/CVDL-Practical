import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Lenna.png')

height, width = image.shape[:2]

center = (width // 2, height // 2)

angle = 120
scale = 1.0

rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imwrite('/kaggle/working/rotated_abd.jpeg', rotated_image)

rotated_image_rgb = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_image_rgb)
plt.axis('off')
plt.show()