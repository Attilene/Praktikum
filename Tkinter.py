from tkinter import *
from math import *


def raw_coords(x, y):
    return [cen[0] + x, cen[1] - y]


def from_polar(ugol, processor=lambda x: x):
    rad = radians(ugol)
    r = processor(rad)
    x = r * cos(rad)
    y = r * sin(rad)
    return x, y


def ball_coords(obj):
    x = (c.coords(obj)[0] + c.coords(obj)[2]) / 2
    y = (c.coords(obj)[1] + c.coords(obj)[3]) / 2
    return x, y


def move(obj, x, y, tail=False):
    x0, y0 = ball_coords(obj)
    x1, y1, x2, y2 = c.coords(obj)
    halfX = (x2 - x1) / 2
    halfY = (y2 - y1) / 2
    c.moveto(obj, *raw_coords(x - halfX, y + halfY))
    x1, y1 = ball_coords(obj)
    if tail:
        c.create_line(x0, y0, x1, y1, fill="black")


def ball_to_centre():
    c.moveto(ball, 290, 290)


def ball_move():
    def act():
        global pos

        def processor(rad):
            return 200
        x, y = from_polar(pos, processor)
        move(ball, x, y)
        pos += step

    actm(act)


def spiral():
    ball_to_centre()

    def act():
        global pos

        def processor(rad):
            return rad * 5
        x, y = from_polar(pos, processor)
        move(ball, x, y, True)
        pos += step

    actm(act)


def flower():
    ball_to_centre()

    def act():
        global pos

        def processor(rad):
            return sin(rad * 6) * 200
        x, y = from_polar(pos, processor)
        move(ball, x, y, True)
        pos += step

    actm(act)


def sinus():
    def act():
        global pos

        def processor(rad):
            return sin(rad * 20) * 30 + 200
        x, y = from_polar(pos, processor)
        move(ball, x, y, True)
        pos += step

    actm(act)


def sinus2():
    def act():
        global pos

        def processor(rad):
            return sin(rad * 10) * 30 + 120
        x, y = from_polar(pos, processor)
        move(ball, x, y, True)
        pos += step

    actm(act)


def apple():
    ball_to_centre()
    pos = 90

    def act():
        nonlocal pos

        def processor(rad):
            return (1 - sin(rad)) * (200 / 2)
        x, y = from_polar(pos, processor)
        move(ball, x, y, True)
        pos += step

    actm(act)


def clover():
    ball_to_centre()

    def act():
        global pos

        def processor(rad):
            return 4 * sin(2 * rad) * 200 / 4
        x, y = from_polar(pos, processor)
        move(ball, x, y, True)
        pos += step

    actm(act)


def actm(anime):
    def actm_move():
        anime()
        root.after(interval, actm_move)
    return actm_move()


cen = [300, 300]
pos = 0
accur = 9
speed = 9
clock = True
step = (-1 if clock else 1) * (4 - (accur / 2.5))
interval = round(abs(-step) * 10 / speed * 5)
root = Tk()
c = Canvas(root, width=600, height=600, bg="yellow")
c.pack()
# okr = c.create_oval(100, 100, 500, 500, fill="red", outline="black")
ball = c.create_oval(490, 290, 510, 310, fill="green", outline="blue")

# ball_move()  # Движение шарика по окружности
# spiral()  # Спиральное движение шарика
# flower()  # Рисование цветка
# sinus()  # Движение по окружности с колебаниями 1
# sinus2()  # Движение по окружности с колебаниями 2
# apple()  # Рисование яблока
clover()  # Четырехлистный клевер

root.mainloop()
