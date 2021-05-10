#!python3
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import random

def image(color=(255,255,255),filename=None):
	if filename:
		return Image.open(filename) 
	return Image.new("RGB", (1920, 1080), color=color)

# size = image.size
img = image()
image_matrix = img.load()


random_pixels = ((random.choice(range(1920)), random.choice(range(1080))) for x in range(2000000))

for pixel in random_pixels:
	image_matrix[pixel[0], pixel[1]]=(0,0,0)

img.show()