#!python3
# -*- coding: utf-8 -*-
import turtle 
from time import sleep
from PIL import Image, ImageDraw
from math import sqrt, atan, degrees, acos
from numpy import arange

def image(color=(255,255,255),filename=None):
    if filename:
        return Image.open(filename) 
    return Image.new("RGB", (1600, 990), color=color)

img = image(filename="image.jpg")
image_matrix = img.load()

def negative(image_matrix):
    for x in range(1920):
        for y in range(1080):
            image_matrix[x,y] = tuple(255-i for i in image_matrix[x,y])

for x in range(1920):
    for y in range(1080):
        rgb = image_matrix[x,y]
        # image_matrix[x,y] = tuple(for i in image_matrix[x,y])
        r,g,b = rgb[0], rgb[1], rgb[2]
        color = [r,g,b]
        image_matrix[x,y] = tuple([x for x in color])

img.show()