from tkinter import *
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
        x = randint(1, size_can[0])
        y = -10
        x_buf = randint(2, 4)
        dict_colors = {"red": [k for k in range(1, 143)], "orange": [k for k in range(143, 286)],
                  "yellow": [k for k in range(286, 428)], "green": [k for k in range(428, 570)],
                  "skyblue": [k for k in range(570, 712)], "blue": [k for k in range(712, 854)],
                  "purple": [k for k in range(854, 1001)]}
        for j in dict_colors:
            if x in dict_colors.get(j):
                colors = j
        # colors = choice(("blue", "white", "skyblue"))
        # colors = "#" + str("%06x" % (16777 * x))
        # colors = "#" + str("%06x" % randint(0, 0xFFFFFF))
        # colors = choice(("yellow", "red", "blue", "green", "orange", "purple", "skyblue"))
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
pl = 3
speedfront = 15
speedback1 = speedfront - 3
speedback2 = speedfront - 6
interval = 5
root = Tk()
c = Canvas(root, width=size_can[0], height=size_can[1], bg="black")
c.pack()
rain()

root.mainloop()