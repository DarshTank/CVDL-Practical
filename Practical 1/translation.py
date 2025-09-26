
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Lenna.png')

height, width = image.shape[:2]

quarter_height, quarter_width = height / 4, width / 4

T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])

img_translation = cv2.warpAffine(image, T, (width, height))

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img_translation_rgb = cv2.cvtColor(img_translation, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Translated Image")
plt.imshow(img_translation_rgb)
plt.axis('off')

plt.show()