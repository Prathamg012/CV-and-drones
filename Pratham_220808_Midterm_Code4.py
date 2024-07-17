import cv2
import numpy as np
import imutils

def shape(s):
    # Load the image
    image = cv2.imread(s)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find contours in the image
    contours, _ = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        # Get approximate polygon
        epsilon = 0.02*cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)

        # Classify shapes based on number of sides
        if len(approx) == 3:
            shape_name = "Triangle"
        elif len(approx) == 4:
            shape_name = "Quadrilateral"
        elif len(approx) == 5:
            shape_name = "Pentagon"
        elif len(approx) == 6:
            shape_name = "Hexagon"
        elif len(approx) == 7:
            shape_name = "Heptagon"
        elif len(approx) == 8:
            shape_name = "Octagon"
        elif len(approx) == 9:
            shape_name = "Nonagon"
        else:
            shape_name = "Circle"

        # Find contour center to place text at the center
        M = cv2.moments(cnt)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        cv2.drawContours(image, [cnt], -1, (0, 255, 0), 2)
        cv2.putText(image, shape_name, (cX-20, cY-20), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255), 2)

    # Show the image
    cv2.imshow("Image", image)
    cv2.waitKey(0)

# Call the function with the path to your image
shape('/Users/prathamgarg/Downloads/types-of-polygons.png')
