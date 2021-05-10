#!python3
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw
from time import sleep
import os

# 	draw = ImageDraw.Draw(img) 
magic_points = ((960, 240), (1260,840), (660, 840))
def image(color=(255,255,255),filename=None):
	if filename:
		return Image.open(filename) 
	return Image.new("RGB", (1920, 1080), color=color)

# size = image.size

img = image()
draw = ImageDraw.Draw(img) 
image_matrix = img.load()
triangle_count=0

def mid(a,b):
	return ((a[0]+b[0])/2, (a[1]+b[1])/2)

def triangles_inside_triangle(a,b,c, limit=3):
	if limit==1:
		return
	m = mid(a,b)
	n = mid(b,c)
	k = mid(a,c)

	draw_triangle(m,n,k)
	triangles_inside_triangle(m,n,k, limit-1)
	triangles_inside_triangle(m,b,n, limit-1)
	triangles_inside_triangle(k,n,c, limit-1)
	triangles_inside_triangle(a,m,k, limit-1)




def sierpintski(a,b,c, limit=3, drawer=draw, points=False):
	global triangle_count
	if limit==1:
		print("Total Triangles: {}".format(triangle_count))
		return
	m = mid(a,b)
	n = mid(b,c)
	k = mid(a,c)

	if points:
		drawer.text(m, "M", fill=(0,0,0))
		drawer.text(n, "N", fill=(0,0,0))
		drawer.text(k, "K", fill=(0,0,0))

	sierpintski(a,k,m, limit-1)
	sierpintski(n,m,b, limit-1)
	sierpintski(c,k,n, limit-1)
	draw_triangle(m,n,k)
	triangle_count+=1

	
def draw_triangle(a, b, c, drawer=draw, points=False):
	if points:
		drawer.text(a, "A", fill=(0,0,0))
		drawer.text(b, "B", fill=(0,0,0))
		drawer.text(c, "C", fill=(0,0,0))

	drawer.line((a[0], a[1], b[0], b[1]), fill=128)
	drawer.line((b[0], b[1], c[0], c[1]), fill=128)
	drawer.line((a[0], a[1], c[0], c[1]), fill=128)

# os.mkdir("sierpintsk")
# os.chdir("sierpintsk")
# for iteration in range(1,8):
# 	img = image()
# 	draw = ImageDraw.Draw(img) 
# 	image_matrix = img.load()
# 	draw_triangle((960, 240), (1260,840), (660, 840))
# 	sierpintski((960, 240), (1260,840), (660, 840), limit=iteration)
# 	img.save("Iteration{}.jpg".format(iteration))
# 	img.show()
# 	sleep(1)
# 	img.close()

iteration = 8
draw_triangle((960, 240), (1260,840), (660, 840))
sierpintski((960, 240), (1260,840), (660, 840), limit=iteration)

img.show()