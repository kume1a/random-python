#!/usr/bin/python
# -*- coding: utf-8 -*-
import turtle
import random
import math
import pyautogui
import os
import shutil
from math import cos, radians, acos, degrees, pi
from time import sleep


run = True
deltaY = 10
startX, startY = (-940, -490)

n0 = 1.5
n = n0

a0 = 60
# deltaN = 0.01
# cosa0 = cos(radians(a0))

def grid(pen, startX, startY, deltaY):
    pen.setheading(0)
    # print("\n[*] Starting to grid")
    for i in range(int(abs(startY*2)/deltaY)):
        y = startY+i*deltaY
        setPos(startX, y, pen)
        pen.forward(abs(startX*2))
    # print("[*] Gridding done")
    return [startY+i*deltaY for i in range(int(abs(490-startY)/deltaY))]
def get_grid(pen, startX, startY, deltaY):

    return [startY+i*deltaY for i in range(int(abs(490-startY)/deltaY))]
def setPos(x,y, pen):
    pen.penup()
    pen.setpos(x,y)
    pen.pendown()

def set_angle(angle, pen):
    pen.setheading(0)
    pen.left(angle)

def get_n(y):
    return n0 * (1-k*y)

def get_alfa(n):
    global run
    try:
        alfa = degrees(acos((n0*cosa0)/n))
        return alfa
    except ValueError:
        print("### Error ###")
        run = False
        return 0

def screenshot(i):
    pyautogui.screenshot("image{}.jpg".format(i), region=(30, 30, 1890, 1000))
    # turtle.resetscreen()
    
def write(content):
    position = pen.pos()
    pen.penup()
    pen.setpos(780, 400)
    pen.write(content, font=("Arial", 18, "normal"))
    pen.setpos(position)
    pen.pendown()


if __name__ == '__main__':
    pen = turtle.Turtle()
    pen.speed(0)
    setPos(x=0, y=0, pen=pen)
    gridY = grid(pen=pen, startX=startX, startY=startY, deltaY=deltaY)

    sleep(2)

    name = "Variable_a0"
    if not os.path.exists(name):
        os.mkdir(name)
    else:
        # os.rmdir(name)
        shutil.rmtree(name)
        os.mkdir(name)
    os.chdir(name)
    i = 0
    cosa0 = cos(radians(a0))
    for deltaN in range(3, 9):
        deltaN = float("0.00{}".format(deltaN))

        set_angle(a0, pen)
        write("a0: {}\nn: {}\ndelta_n: {}".format(a0, n0, deltaN))
        setPos(x=-940, y=-490, pen=pen)

        while run:
            if round(pen.ycor()) in gridY:
                n -= deltaN
                angle = get_alfa(n)
                set_angle(angle, pen)

                # print("alfa: {}\nN: {}\n".format(round(angle, 4), round(n, 4)))
            y = pen.pos()[1]
            if y>490:
                break
            pen.forward(1)

        pen.pendown()

        n = n0
        run = True
        i+=1

        screenshot(i)

        turtle.resetscreen()
        pen = turtle.Turtle()
        pen.speed(0)

        setPos(x=0, y=0, pen=pen)
        gridY = grid(pen=pen, startX=startX, startY=startY, deltaY=deltaY)
        
    turtle.exitonclick()