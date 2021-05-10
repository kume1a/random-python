import turtle 

# def draw_hexagon (t, size):
#     n=6
#     angle= 360/n
#     for i in range(n):
#         t.forward(size)
#         t.left(angle)

# turtle.colormode(255)
# mega=turtle.Turtle()
# mega.speed(0) 
# leng = 100
# g = 0
# for i in range(30):
#     r = 5+(i*10)
#     g = 0
#     b = 0
#     color = (r, g, b)
#     if r>255:
#         break
#     mega.fillcolor(color) 
#     mega.begin_fill()
#     draw_hexagon(mega, leng)
#     mega.end_fill()
#     leng = leng + 5
#     mega.left(5)


pen = turtle.Turtle()
if __name__ == '__main__':
    pen.setpos(0,450)
    pen.write("20", font=("Arial", 16, "normal"))
    turtle.mainloop()