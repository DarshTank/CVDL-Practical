import cv2
import numpy as np

img = cv2.imread('samplegray.jpeg')


gamma = 1.2

gamma_image = np.array(255 * (img / 255) ** gamma, dtype='uint8')
    
output_filename = f'gamma_transformed{gamma}.jpg'

cv2.imwrite(output_filename, gamma_image)
print(f"Saved gamma-corrected image: {output_filename}")
    
cv2.imshow(f'Gamma Corrected (gamma={gamma})', gamma_image)
cv2.waitKey(0)

cv2.destroyAllWindows()