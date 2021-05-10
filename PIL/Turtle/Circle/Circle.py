import json
import turtle
import time
import math
import os
import pyautogui

turtle.colormode(255)
def draw_line(a, b, pen):
    pen.penup()
    pen.goto(a)
    pen.pendown()
    pen.goto(b)

def get_points(pen, r, n):    
    angle = 360/n
    points = []
    pen.setpos(0,0)
    pen.penup()

    now = time.time()
    pen.forward(r)
    pen.right(angle)
    pen.setpos(0,0)
    time_for_one = time.time()-now
    print("Estimated time: {} sec".format(round(time_for_one*n, 3)))

    for point in range(n):
        pen.forward(r)
        points.append(pen.pos())
        pen.right(angle)
        pen.setpos(0,0)

    return points

def draw(pen, mult, points):
    l = len(points)
    r = 0
    g = 0
    b = 0
    print("Estimated time: {} sec".format(round(l*0.05615321397781372, 3)))
    for i,point in enumerate(points):
        # r+=1
        # b+=5
        # g+=1
        if r>255:
            r=0
        if g>255:
            g=0
        if b>255:
            b=0
        pen.color((r,g,b))
        # dest = int(math.sqrt(i)**mult)
        dest = int(i*mult)
        if dest>l-1:
            dest = dest - dest//l*l
        draw_line(points[i], points[dest], pen)

if __name__ == "__main__":  
    pen = turtle.Turtle()
    pen.speed(0)
    now = time.time()

    # print("[+] Getting Points")
    # points = get_points(pen, 400, 350)
    # with open('data.json', 'w', encoding='utf-8') as file:
    #     json.dump(points, file, ensure_ascii=False, indent=4)
    # exit()

    with open("data.json", "r") as file:
        points = json.load(file)

    # print("## Done ##\n")
    # print("[+] Starting to Draw")

    name = "Test"
    if not os.path.exists(name):
        os.mkdir(name)
    else:
        os.rmdir(name)
        os.mkdir(name)
    os.chdir(name)

    i = .1
    time.sleep(3)
    while i < 30:
        # points = get_points(pen, 400, i)
        draw(pen, i, points)

        pen.penup()
        pen.setpos(-10, 440)
        pen.pendown()
        pen.write(int(i), font=("Arial", 18, "normal"))

        i += .1

        pyautogui.screenshot("image{}.jpg".format(i), region=(30, 30, 1890, 1000))

        turtle.resetscreen()
        pen.speed(0)

    # print("## Done ##")
    # print("\nFinished execution in {} sec\n".format(round(time.time()-now, 3)))

    try:
        turtle.exitonclick()
    except turtle.Terminator:
        pass
# style = ('Courier', 30, 'italic')
# turtle.write('3', font=style, align='center')