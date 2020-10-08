from tkinter import *
from random import *


def point_coords(obj):
    x = (c.coords(obj)[0] + c.coords(obj)[2]) / 2
    y = (c.coords(obj)[1] + c.coords(obj)[3]) / 2
    return x, y


def create_line(x0, y0, obj):
    x1, y1 = point_coords(obj)
    # colors = "white"
    colors = "#" + str("%06x" % randint(0, 0xFFFFFF))
    # colors = choice(("yellow", "red", "blue", "green", "orange", "purple", "skyblue"))
    # colors = choice(("blue", "white", "skyblue"))
    c.create_line(x0, y0, x1, y1, fill=colors)


def way(obj):
    def act():
        x0, y0 = point_coords(obj)
        if direction == "right":
            c.move(obj, randint(0, 1) * step, randint(-1, 1) * step)
        elif direction == "left":
            c.move(obj, randint(-1, -0) * step, randint(-1, 1) * step)
        elif direction == "up":
            c.move(obj, randint(-1, 1) * step, randint(-1, 0) * step)
        elif direction == "down":
            c.move(obj, randint(-1, 1) * step, randint(0, 1) * step)
        else:
            c.move(obj, randint(-1, 1) * step, randint(-1, 1) * step)
        create_line(x0, y0, obj)
        # assert (x0 < size_can[0] - 100) or finish

    actm(act)


def actm(anime):
    def actm_move():
        global finish
        try:
            anime()
            root.after(interval, actm_move)
        except AssertionError:
            print("Finish")
            finish = True

    return actm_move()


finish = False
size_can = [800, 800]
step = 3
interval = 10
direction = "none"
root = Tk()
c = Canvas(root, width=size_can[0], height=size_can[1], bg="black")
# c.create_line(size_can[0] - 100, 0, size_can[0] - 100, 800, fill="white")
point1 = c.create_oval(0, 0, 0, 0, fill="black", outline="black")
# point2 = c.create_oval(0, 0, 0, 0, fill="black", outline="black")
c.move(point1, size_can[0] / 2, size_can[1] / 2)
# c.move(point1, 0, size_can[1] / 4)
# c.move(point2, 0, size_can[1] * 3 / 4)
c.pack()
way(point1)
# way(point2)

root.mainloop()