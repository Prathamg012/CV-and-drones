import cv2
import numpy as np

def ig_filter(s):

    bright = cv2.convertScaleAbs(s, alpha=0.5, beta=0)


    contrast = cv2.convertScaleAbs(bright, alpha=1.5, beta=128 * (1 - 1.5))


    hsv = cv2.cvtColor(contrast, cv2.COLOR_BGR2HSV)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * 1.5, 0, 255).astype(np.uint8)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


    # Load an image
image = cv2.imread('/Users/prathamgarg/Downloads/Landscape-Photography-steps.jpg')
modified = ig_filter(image)
    
cv2.imshow('Original Image', image)
cv2.imshow('Modified Image', modified)
cv2.waitKey(0)
    


