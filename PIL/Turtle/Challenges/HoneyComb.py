import turtle 
from random import choice

def pos(x,y):
    pen.penup()
    pen.setpos(x,y)
    pen.pendown()

def hexagon(x,y,l):
    pos(x,y)
    pen.setheading(0)
    for side in range(6):
        pen.forward(l)
        pen.left(60)

def get_points(x,y,n,l):
    rows1, rows2 = [], []
    pos(x,y)
    pen.penup()
    for _ in range(n):
        pen.setheading(0)
        rows1.append(pen.pos())
        pen.left(120)
        pen.forward(l)
        rows2.append((pen.pos()[0]+2*l, pen.pos()[1]))
        pen.right(60)
        pen.forward(l)
    pen.pendown()
    return zip(rows1, rows2)

def honeycomb(x,y,n,l):
    print("Starting point: ({},{})\nRows: {}\n".format(x,y,n))

    i = 0
    colors = ["#FF7F00","#FF9000",
              "#FF8C00","#FF9D00",
              "#FFAA00","#FFB600",
              "#FFCC00","#FFD400",
              "#FFD800","#FFE900"
    ]
    print("[+] Getting Points\n")
    points = get_points(x,y,n,l)
    for point1,point2 in points:
        i+=1
        print("Drawing row {}".format(i))
        for num in range(0,3*n,3):
            pen.color(choice(colors))

            pen.begin_fill()
            hexagon(point1[0]+num*l, point1[1], l)
            pen.end_fill()
            pen.begin_fill()
            hexagon(point2[0]+num*l, point2[1], l)
            pen.end_fill()

if __name__ == '__main__':
    pen = turtle.Turtle()
    pen.speed(0)
    honeycomb(-300,-200,12,20)    
    turtle.exitonclick()