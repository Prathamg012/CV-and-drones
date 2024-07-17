# Python program to illustrate HoughLine
# method for line detection
import cv2
import numpy as np

def hough_line(s):
	img = cv2.imread(s)


	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# Apply edge detection method on the image
	edges = cv2.Canny(gray, 50, 150, apertureSize=3)

	# This returns an array of r and theta values
	lines = cv2.HoughLines(edges, 1, np.pi/180, 100)

	# The below for loop runs till r and theta values
	# are in the range of the 2d array
	for r_theta in lines:
		arr = np.array(r_theta[0], dtype=np.float64)
		r, theta = arr
		# Stores the value of cos(theta) in a
		a = np.cos(theta)

		# Stores the value of sin(theta) in b
		b = np.sin(theta)

		# x0 stores the value rcos(theta)
		x0 = a*r

		# y0 stores the value rsin(theta)
		y0 = b*r

		# x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
		x1 = int(x0 + 1000*(-b))

		# y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
		y1 = int(y0 + 1000*(a))

		# x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
		x2 = int(x0 - 1000*(-b))

		# y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
		y2 = int(y0 - 1000*(a))

		
		cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
	return img
# All the changes made in the input image are finally
# written on a new image houghlines.jpg
path = '/Users/prathamgarg/Downloads/istockphoto-1186721311-612x612.jpg'
mod = hough_line(path)

cv2.imshow('original',cv2.imread(path))
cv2.imshow('final',mod)
cv2.waitKey(0)
