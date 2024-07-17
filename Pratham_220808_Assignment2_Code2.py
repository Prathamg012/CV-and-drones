from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import math
import cv2
import Pratham_220808_Assignment2_Code1 as pr


def rotate(img,y):
    rotated_image = img.rotate(y) #angle is in degrees
    return rotated_image

def rotatedFlags():
    global rotated_0
    rotated_0 = flag.rotate(0)
    global rotated_90 
    rotated_90 = flag.rotate(90)
    global rotated_180 
    rotated_180 = flag.rotate(180)
    global rotated_270 
    rotated_270 = flag.rotate(270)
    # plt.figure()
    # plt.imshow(rotated_0)
    # plt.figure()
    # plt.imshow(rotated_90)
    # plt.figure()
    # plt.imshow(rotated_180)
    # plt.figure()
    # plt.imshow(rotated_270)
    # plt.show()
    return (rotated_0,rotated_90,rotated_180,rotated_270)
    
   
flag = pr.flag
r0,r90,r180,r270 = rotatedFlags()


