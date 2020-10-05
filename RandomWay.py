from tkinter import *
from random import *


def point_coords():
    x = (c.coords(point)[0] + c.coords(point)[2]) / 2
    y = (c.coords(point)[1] + c.coords(point)[3]) / 2
    return x, y


def create_line(x0, y0):
    x1, y1 = point_coords()
    colors = "white"
    # colors = choice(("yellow", "red", "blue", "green", "orange", "purple", "skyblue"))
    # colors = choice(("blue", "white", "skyblue"))
    c.create_line(x0, y0, x1, y1, fill=colors)


def way():
    def act():
        x0, y0 = point_coords()
        if direction == "right":
            c.move(point, randint(0, 1) * step, randint(-1, 1) * step)
        elif direction == "left":
            c.move(point, randint(-1, -0) * step, randint(-1, 1) * step)
        elif direction == "up":
            c.move(point, randint(-1, 1) * step, randint(-1, 0) * step)
        elif direction == "down":
            c.move(point, randint(-1, 1) * step, randint(0, 1) * step)
        else:
            c.move(point, randint(-1, 1) * step, randint(-1, 1) * step)
        create_line(x0, y0)

    actm(act)


def actm(anime):
    def actm_move():
        anime()
        root.after(interval, actm_move)

    return actm_move()


size_can = [800, 800]
step = 3
interval = 10
direction = "none"
root = Tk()
c = Canvas(root, width=size_can[0], height=size_can[1], bg="black")
point = c.create_oval(0, 0, 1, 1, fill="black", outline="black")
c.move(point, size_can[0] / 2, size_can[1] / 2)
c.pack()
way()

root.mainloop()