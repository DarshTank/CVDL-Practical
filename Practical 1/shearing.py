import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Lenna.png')

height, width = image.shape[:2]


shear_x = 0.3
shear_y = 0.0 

shear_matrix = np.float32([
    [1, shear_x, 0],
    [shear_y, 1, 0]
])

sheared_image = cv2.warpAffine(image, shear_matrix, (width, height))

cv2.imwrite('/kaggle/working/sheared_rotated_abd.jpeg', sheared_image)

sheared_image_rgb = cv2.cvtColor(sheared_image, cv2.COLOR_BGR2RGB)
plt.imshow(sheared_image_rgb)
plt.axis('off')
plt.show()