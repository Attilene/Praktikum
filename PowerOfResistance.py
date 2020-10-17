from tkinter import *
from random import *
import math


def powerOfResistance():
    global balls
    create_Balls()

    def act():
        for i in range(len(balls)):
            if balls[i][3]:
                if balls[i][2]:
                    c.move(balls[i][0], 0, balls[i][4] * 4)
                    if balls[i][6] >= balls[i][2][-1]:
                        if balls[i][5] == 2:
                            balls[i][2].pop()
                            balls[i][5] = 1
                        else:
                            balls[i][5] += 1
                        balls[i][4] *= -1
                        balls[i][6] = 1
                    balls[i][6] += 2
                else:
                    c.move(balls[i][0], 0, -1 * (c.coords(balls[i][0])[3] - size_can[1]))
                    continue
            elif c.coords(balls[i][0])[3] >= size_can[1]:
                c.move(balls[i][0], 0, -1 * (c.coords(balls[i][0])[3] - size_can[1]))
                balls[i][3] = True
            elif c.coords(balls[i][0])[3] >= size_can[1] / 2 + balls[i][7]:  # Проверка на погружение + учет инерции тела
                c.move(balls[i][0], 0, balls[i][8])  # Скорость передвижения шарика с учетом его размера
            elif not balls[i][3]:
                c.move(balls[i][0], 0, speed + 5)

    actm(act)


def create_Balls():
    for i in range(amount):
        x = randint(1, size_can[0] - 50)
        y = -100
        x_buf = randint(20, 81)
        # colors = choice(("blue", "white", "skyblue"))
        # colors = "#" + str("%06x" % (16777 * x))
        # colors = "#" + str("%06x" % randint(0, 0xFFFFFF))
        # colors = choice(("yellow", "red", "blue", "green", "orange", "purple", "skyblue"))
        colors = "blue"
        # colors = choice(["pink", "purple", "violet"])
        balls.append([c.create_oval(x, y, x + x_buf, y + x_buf, outline=colors, width=3), x_buf,
                      [i for i in range(1, x_buf // 10, 2)], False, -1, 1, 1,
                      (speed * density_ball * (4/3 * math.pi * math.pow(x_buf / 200, 3))) / (speed * 2),
                      0.2 * math.sqrt(x_buf / 100 * (density_ball - density_liquid))])


def actm(anime):
    def actm_move():
        anime()
        root.after(interval, actm_move)

    return actm_move()


balls = []
size_can = [700, 650]
density_ball = 1500
density_liquid = 1000
amount = 10
speed = 1
interval = 10
root = Tk()
c = Canvas(root, width=size_can[0], height=size_can[1], bg="white")
c.pack()
c.create_rectangle(0, size_can[1] / 2, size_can[0] + 20, size_can[0] + 20, fill="skyblue", outline="skyblue")
powerOfResistance()

root.mainloop()