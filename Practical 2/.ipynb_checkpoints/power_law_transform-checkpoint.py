import cv2
import numpy as np

image = cv2.imread('samplegray.jpeg')
print("The original image:")
cv2.imshow("Original Image", image)

gamma = 1
c = 255.0 / (255.0 ** gamma)

image_float = image / 255.0
power_law_transformed = c * np.power(image_float, gamma)
power_law_transformed = np.uint8(power_law_transformed * 255)

print("The power-law transformation of the image:")
cv2.imshow("Power-Law Transformed Image", power_law_transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()
