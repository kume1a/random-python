import turtle

screen = turtle.Screen()
# image = "rocketship.png"
# screen.addshape(image)
# turtle.shape(image)

pen = turtle.Turtle()
pen.penup()

pen.color("red")
screen.bgcolor("#000000")

move_speed = 10

def up():
    pen.setheading(90)

def down():
    pen.setheading(270)

def left():
    pen.setheading(180)

def right():
    pen.setheading(0)

def done():
    turtle.done()



screen.onkey(done, "q")
screen.onkey(up, "w")
screen.onkey(down, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.listen()

while True:
    pen.forward(3)

    x,y = pen.pos()
    if x>955:
        turtle.ht()
        pen.setpos(-955, y)
    elif x<-955:
        turtle.ht()
        pen.setpos(955, y)
    elif y>535:
        turtle.ht()
        pen.setpos(x,-535)
    elif y<-535:
        turtle.ht()
        pen.setpos(x,535)
                

turtle.done()