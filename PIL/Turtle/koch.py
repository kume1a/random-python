#!python3
# -*- coding: utf-8 -*-
from turtle import *


def snowflake(lengthSide, levels): 
    if levels == 0: 
        forward(lengthSide) 
        return
    lengthSide /= 3.0
    snowflake(lengthSide, levels-1) 
    left(60) 
    snowflake(lengthSide, levels-1) 
    right(120) 
    snowflake(lengthSide, levels-1) 
    left(60) 
    snowflake(lengthSide, levels-1) 
  
if __name__ == "__main__": 
  
    speed(0)                    
    length = 1600.0              
    penup()                      
    backward(length/2.0)         
    pendown()          
    snowflake(length, 6)   

    mainloop()  

turtle.done()