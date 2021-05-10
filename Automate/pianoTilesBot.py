#!python3
# -*- encoding: utf-8 -*-

from pyautogui import click
from PIL import ImageGrab
import numpy as np 
from time import sleep

BLACK = np.array([0,0,0])
positions = ((650, 735), (650, 880), (650, 1020), (650, 1150))

image = np.array(ImageGrab.grab())
click(1254,1060)
sleep(2)

for a in range(2000):
    sleep(.1)
    image = np.array(ImageGrab.grab())
    for y,x in positions:
        if (image[y][x]==BLACK).all():
            print("click")