#!python3
# -*- encoding: utf-8 -*-

import turtle
import math


def normalize(angle):
    return angle-(angle//360*360)

angles = [0]
def generate_angles(n):
    global angles
    angles.extend([normalize(x+90) for x in angles])
    print(angles)
    if n<=1:
        return
    generate_angles(n-1)

def levy(angles, l):
    startAngle = normalize(360-45*(len(angles)**(1/3)))

    for angle in angles:
        pen.setheading(startAngle)
        pen.left(angle)
        pen.forward(l)


if __name__=="__main__":
    # Change this values
    recursiveValue = 13
    length = 3

    screen = turtle.Screen()
    pen = turtle.Turtle()
    screen.bgcolor("#000000")
    pen.color("#ffffff")
    pen.speed(0)

    generate_angles(recursiveValue)
    levy(angles, length)
    
    turtle.exitonclick()