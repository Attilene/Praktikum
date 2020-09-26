from tkinter import *
from math import *
from random import *


def rain():
    global drops

    def act():
        l = len(drops)
        create_drop()
        for i in range(l):
            if drops[i][1] == 2:
                c.move(drops[i][0], 0, speedfront)
            else:
                c.move(drops[i][0], 0, speedback)
        if c.coords(drops[0][0])[1] > size_can[1] + 100:
            for i in range(pl):
                c.delete(drops[i][0])
                drops.pop(i)

    actm(act)


def create_drop():
    for i in range(pl):
        x = randint(2, size_can[0])
        y = -10
        x_buf = randint(1, 2)
        drops.append([c.create_rectangle(x, y, x + x_buf, x_buf + y + 25, fill="blue", outline="blue"), x_buf])


def actm(anime):
    def actm_move():
        anime()
        root.after(interval, actm_move)

    return actm_move()


drops = []
size_can = [1000, 600]
pl = 10
accur = 5
speedfront = 15
speedback = speedfront - 4
step = accur / 3 - 4
interval = round(abs(step) * 10 / speedfront * 5)
root = Tk()
c = Canvas(root, width=size_can[0], height=size_can[1], bg="white")
c.pack()
rain()

root.mainloop()
