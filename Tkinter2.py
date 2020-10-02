from tkinter import *
from math import *
from random import *


def rain():
    global drops

    def act():
        l = len(drops)
        create_drop()
        for i in range(l):
            if drops[i][1] == 4:
                c.move(drops[i][0], 0, speedfront)
            elif drops[i][1] == 3:
                c.move(drops[i][0], 0, speedback1)
            else:
                c.move(drops[i][0], 0, speedback2)
        if c.coords(drops[0][0])[1] > size_can[1] + 100:
            for i in range(pl):
                c.delete(drops[i][0])
                drops.pop(i)

    actm(act)


def create_drop():
    for i in range(pl):
        x = randint(2, size_can[0])
        y = -10
        x_buf = randint(2, 4)
        colors = choice(("blue", "white", "skyblue"))
        # colors = "blue"
        # colors = choice(["pink", "purple", "violet"])
        drops.append([c.create_oval(x, y, x + x_buf, x_buf * 3 + y + 15, fill=colors, outline=colors), x_buf])


def actm(anime):
    def actm_move():
        anime()
        root.after(interval, actm_move)

    return actm_move()


drops = []
size_can = [1000, 600]
pl = 10
accur = 5
speedfront = 20
speedback1 = speedfront - 4
speedback2 = speedfront - 8
step = accur / 3 - 4
interval = round(abs(step) * 10 / speedfront * 5)
root = Tk()
c = Canvas(root, width=size_can[0], height=size_can[1], bg="black")
c.pack()
rain()

root.mainloop()
