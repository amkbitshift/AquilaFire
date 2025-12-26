import cv2
import numpy as np

def smoke_color_score(image_path):
    img = cv2.imread(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Smoke-like colors: low saturation, mid-high value
    mask = cv2.inRange(
        hsv,
        (0, 0, 120),    # low saturation
        (180, 60, 255)
    )

    smoke_pixels = np.sum(mask > 0)
    total_pixels = img.shape[0] * img.shape[1]

    return smoke_pixels / total_pixels
