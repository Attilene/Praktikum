from tkinter import *
from random import *
import math


class PowerOfResistance:
    balls = []
    size_can = [700, 650]
    density_ball = 1500
    density_liquid = 1000
    amount = 10
    speed = 1
    interval = 10
    # colors = choice(("blue", "white", "skyblue"))
    # colors = "#" + str("%06x" % (16777 * x))
    # colors = "#" + str("%06x" % randint(0, 0xFFFFFF))
    # colors = choice(("yellow", "red", "blue", "green", "orange", "purple", "skyblue"))
    colors = "blue"
    # colors = choice(["pink", "purple", "violet"])

    def __init__(self, root):
        self.root = root
        self.root.wm_title("Power of Resistense")

    def __createCanvas(self):
        c = Canvas(self.root, width=self.size_can[0], height=self.size_can[1], bg="white")
        c.pack()
        c.create_rectangle(0, self.size_can[1] / 2, self.size_can[0] + 20, self.size_can[0] + 20, fill="skyblue", outline="skyblue")
        return c

    def powerOfResistance(self):
        c = self.__createCanvas()
        self.__create_Balls(c)

        def act():
            for i in range(len(self.balls)):
                if self.balls[i][3]:
                    if self.balls[i][2]:
                        c.move(self.balls[i][0], 0, self.balls[i][4] * 4)
                        if self.balls[i][6] >= self.balls[i][2][-1]:
                            if self.balls[i][5] == 2:
                                self.balls[i][2].pop()
                                self.balls[i][5] = 1
                            else:
                                self.balls[i][5] += 1
                            self.balls[i][4] *= -1
                            self.balls[i][6] = 1
                        self.balls[i][6] += 2
                    else:
                        c.move(self.balls[i][0], 0, -1 * (c.coords(self.balls[i][0])[3] - self.size_can[1]))
                        continue
                elif c.coords(self.balls[i][0])[3] >= self.size_can[1]:
                    c.move(self.balls[i][0], 0, -1 * (c.coords(self.balls[i][0])[3] - self.size_can[1]))
                    self.balls[i][3] = True
                elif c.coords(self.balls[i][0])[3] >= self.size_can[1] / 2 + self.balls[i][7]:  # Проверка на погружение + учет инерции тела
                    c.move(self.balls[i][0], 0, self.balls[i][8])  # Скорость передвижения шарика с учетом его размера
                elif not self.balls[i][3]:
                    c.move(self.balls[i][0], 0, self.speed + 5)

        self.actm(act)

    def __create_Balls(self, c):
        for i in range(self.amount):
            x = randint(1, self.size_can[0] - 50)
            y = -100
            x_buf = randint(20, 81)
            self.balls.append([c.create_oval(x, y, x + x_buf, y + x_buf, outline=self.colors, width=3), x_buf,
                          [i for i in range(1, x_buf // 10, 2)], False, -1, 1, 1,
                          (self.speed * self.density_ball * (4/3 * math.pi * math.pow(x_buf / 200, 3))) / (self.speed * 2),
                          0.2 * math.sqrt(x_buf / 100 * (self.density_ball - self.density_liquid))])

    def actm(self, anime):
        def actm_move():
            anime()
            root.after(self.interval, actm_move)

        return actm_move()


root = Tk()
powerOfResistance = PowerOfResistance(root)
powerOfResistance.powerOfResistance()
root.mainloop()