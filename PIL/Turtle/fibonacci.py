import turtle 
import math 
  
def fiboPlot(n): 
    a = 0
    b = 1
    square_a = a 
    square_b = b 
  
    x.pencolor("blue") 
  
    x.forward(b * factor) 
    x.left(90) 
    x.forward(b * factor) 
    x.left(90) 
    x.forward(b * factor) 
    x.left(90) 
    x.forward(b * factor) 
  
    temp = square_b 
    square_b = square_b + square_a 
    square_a = temp 
      
    for i in range(1, n): 
        x.backward(square_a * factor) 
        x.right(90) 
        x.forward(square_b * factor) 
        x.left(90) 
        x.forward(square_b * factor) 
        x.left(90) 
        x.forward(square_b * factor) 
  
        temp = square_b 
        square_b = square_b + square_a 
        square_a = temp 
  
    x.penup() 
    x.setposition(factor, 0) 
    x.seth(0) 
    x.pendown() 
  
    x.pencolor("red") 
  
    x.left(90) 
    for i in range(n): 
        print(b) 
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90): 
            x.forward(fdwd) 
            x.left(1) 
        temp = a 
        a = b 
        b = temp + b 
  

if __name__ == "__main__": 
    factor = 10
    n = 15

    x = turtle.Turtle() 
    x.speed(0) 
    fiboPlot(n) 
    turtle.exitontouch() 