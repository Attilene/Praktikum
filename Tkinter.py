from tkinter import *
from math import *


def raw_coor(x, y):
    return [cen[0] + x, cen[1] - y]


def from_polar(ugol, processor=lambda x: x):
    rad = radians(ugol)
    r = processor(rad)
    x = r * cos(rad)
    y = r * sin(rad)
    return x, y


def move(obj, x, y):
    x1, y1, x2, y2 = c.coords(obj)
    halfX = (x2 - x1) / 2
    halfY = (y2 - y1) / 2
    c.moveto(obj, * raw_coor(x - halfX, y + halfY))


def ball_move():
    def action():
        global pos
        def processor(rad): return 200
        x, y = from_polar(pos, processor)
        move(ball, x, y)
        pos += step

    def loopm():
        action()
        root.after(interval, loopm)

    return loopm()


def spiral():
    def act():
        global pos
        r = radians(pos)
        x = r * cos(r)
        y = r * sin(r)
        move(ball, x, y)
        pos += step

    def actm():
        act()
        root.after(interval, actm)

    return actm()


cen = [300, 300]
pos = 0
accur = 2
speed = 10
clw = True
step = (-1 if clw else 1) * (1 - (accur / 2.5))
interval = round(-step * 10 / speed * 5)
root = Tk()
c = Canvas(root, width=600, height=600, bg="yellow")
c.pack()
okr = c.create_oval(100, 100, 500, 500, fill="red", outline="red")
ball = c.create_oval(290, 90, 310, 110, fill="blue", outline="blue")

ball_move()  # Движение шарика по окружности
spiral()  # Спиральное движение шарика

root.mainloop()
