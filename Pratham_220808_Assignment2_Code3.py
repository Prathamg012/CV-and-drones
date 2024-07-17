import matplotlib.pyplot as plt
import numpy as np
import Pratham_220808_Assignment2_Code2 as pr
from PIL import Image
import cv2

def unskew(s):
    img = pr.r0
    
    wid,height = img.size
    #vertical array
    vertical = []
    v = 0
    for i in range(height):
        if i==0:
            vertical.append(img.getpixel((wid/2,0)))
        elif (vertical[v] != img.getpixel((wid/2,i))) and img.getpixel((wid/2,i)) != ((0,0,255)and(0,0,0)):
            v = v+1
            vertical.append(img.getpixel((wid/2,i)))
    if v == 2:
        if vertical[0] == (255,165,0):
            return pr.r0
        elif vertical[0] == (0,128,0):
            return pr.r180
     
        
    #horizotal array
    horizontal = []
    h = 0
    for i in range(wid):
        if i==0:
            horizontal.append(img.getpixel((0,height/2)))
        elif (horizontal[h] != img.getpixel((i,height/2))) and img.getpixel((i,height/2)) != ((0,0,255)and(0,0,0)):
            h = h+1
            horizontal.append(img.getpixel((i,height/2)))
    if h == 2:
        if horizontal[0] == (255,165,0):
            return pr.r90
        elif horizontal[0] == (0,128,0):
            return pr.r270





input = '/Users/prathamgarg/Downloads/output.jpg'
output = unskew(input)
# print(output)
plt.imshow(output)