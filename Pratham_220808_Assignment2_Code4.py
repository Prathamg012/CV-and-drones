import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('/Users/prathamgarg/Downloads/left04.jpg')
h,  w = img.shape[:2]
mtx = np.array([[632.89988921,0.,257.96968956],[  0.,657.3036996,  236.63918698],[  0.,0.,1.]])
dist = np.array([-0.47904946,0.47073016,0.00118414,0.0515523,-1.05946534])
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

# undistort
mapx, mapy = cv.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w,h), 5)
dst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)
# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv.imshow('undistorted',dst)
cv.imshow('original',img)
cv.waitKey(0)


