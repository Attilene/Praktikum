from tkinter import *
from math import *


def ball_move():
    x1 = c.coords(ball)[0]
    y1 = c.coords(ball)[1]
    ug = 90
    while True:
        ug -= 1
        x2 = rad * cos(radians(ug))
        y2 = rad * sin(radians(ug))
        c.move(ball, x2 - x1, y2 - y1)
        x1 = x2
        y1 = y2


root = Tk()
rad = radians(200)
cen = [500, 500]
c = Canvas(root, width=600, height=600, bg="yellow")
c.pack()
okr = c.create_oval(100, 100, 500, 500, fill="red", outline="red")
ball = c.create_oval(290, 90, 310, 110, fill="blue", outline="blue")
# ball_move()
root.mainloop()
