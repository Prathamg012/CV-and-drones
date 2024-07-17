from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import math

def generate():
    height = 600
    width = 600
    image = Image.new("RGB", (width,height), "#FFFFFF")
    draw = ImageDraw.Draw(image)

    draw.rectangle([0,0,width,height/3],fill='orange')

    draw.rectangle([0,400,width,height],fill='green')


    draw.ellipse([200,200,400,400],outline='blue',width=2)


    angle = (2*math.pi)/24
    for i in range(24):
        x1 = 300 + 100*math.cos(angle*i)
        y1 = 300 +100*math.sin(angle*i)
        draw.line([300,300,x1,y1],fill='blue',width=1)
    
    return image

global flag 
flag = generate()
