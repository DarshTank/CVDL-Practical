import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math
import os

def load_image(path):
    # Simple image loader using matplotlib (no OpenCV/PIL)
    img = plt.imread(path)
    if img.dtype == np.float32 or img.dtype == np.float64:
        img = (img * 255).astype(np.uint8)
    return img

def rotate_image(img, angle_deg):
    angle_rad = math.radians(angle_deg)
    cos_theta = math.cos(angle_rad)
    sin_theta = math.sin(angle_rad)
    h, w = img.shape[:2]

    # Use math.ceil to avoid truncation
    new_h = int(math.ceil(abs(h * cos_theta) + abs(w * sin_theta)))
    new_w = int(math.ceil(abs(w * cos_theta) + abs(h * sin_theta)))

    # Center of original and new image
    orig_cx, orig_cy = w // 2, h // 2
    new_cx, new_cy = new_w // 2, new_h // 2

    # Create new blank image
    if img.ndim == 3:
        rotated = np.zeros((new_h, new_w, img.shape[2]), dtype=img.dtype)
    else:
        rotated = np.zeros((new_h, new_w), dtype=img.dtype)

    for y in range(new_h):
        for x in range(new_w):
            # Coordinates in the rotated image
            tx = x - new_cx
            ty = y - new_cy

            # Inverse rotation to find corresponding source pixel
            orig_x = int(round(cos_theta * tx + sin_theta * ty + orig_cx))
            orig_y = int(round(-sin_theta * tx + cos_theta * ty + orig_cy))

            if 0 <= orig_x < w and 0 <= orig_y < h:
                rotated[y, x] = img[orig_y, orig_x]

    return rotated

# Example usage
img = load_image('Lenna.png')
rotated_img = rotate_image(img, 45)  # Rotate by 45 degrees

plt.subplot(1,2,1)
plt.title("Original")
if img.ndim == 2:
    plt.imshow(img, cmap='gray')
else:
    plt.imshow(img)
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Rotated")
if rotated_img.ndim == 2:
    plt.imshow(rotated_img, cmap='gray')
else:
    plt.imshow(rotated_img)
plt.axis('off')

plt.savefig('rotated_output.png')  # Save the figure as an image file

# Display the saved image using the default image viewer (Windows only)
os.startfile('rotated_output.png')