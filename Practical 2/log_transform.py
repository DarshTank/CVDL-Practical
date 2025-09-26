import cv2
import numpy as np

def log_transform_image(input_path, output_path, grayscale=False):
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE if grayscale else cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError(f"Could not load image at {input_path}")

    c = 255.0 / np.log(1 + np.max(img))

    log_transformed = c * np.log(1 + img)

    log_transformed = np.clip(log_transformed, 0, 255).astype(np.uint8)

    success = cv2.imwrite(output_path, log_transformed)
    if not success:
        raise IOError(f"Failed to save image at {output_path}")
    
    print(f"Transformed image saved to {output_path}")

try:
    log_transform_image('rcb.webp', 'log_transformed.png', grayscale=False)
except Exception as e:
    print(f"Error: {e}")