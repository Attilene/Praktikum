from tkinter import *
from random import *
import math


class Attraction:
    balls = []
    size_can = [600, 600]
    amount = 1000
    speed = 1
    interval = 10
    # colors = choice(("blue", "white", "skyblue"))
    # colors = "#" + str("%06x" % (16777 * x))
    # colors = "#" + str("%06x" % randint(0, 0xFFFFFF))
    # colors = choice(("yellow", "red", "blue", "green", "orange", "purple", "skyblue"))
    colors = "white"
    # colors = choice(["pink", "purple", "violet"])

    def __init__(self, root):
        self.root = root
        self.root.wm_title("Attraction")

    def __createCanvas(self):
        c = Canvas(self.root, width=self.size_can[0], height=self.size_can[1], bg="black")
        c.pack()
        c.create_oval(self.size_can[0] / 2, self.size_can[1] / 2, self.size_can[0] / 2 + 5, self.size_can[1] / 2 + 5,
                      fill=self.colors, outline="black")
        return c

    def attraction(self):
        c = self.__createCanvas()
        self.__create_Balls(c)

        def act():
            for i in self.balls:
                if pow(c.coords(i[0])[0] - self.size_can[0] / 2, 2) + pow(c.coords(i[0])[1] - self.size_can[1] / 2, 2) <= 6400:
                    print(c.coords(i[0]))
                    c.move(i[0], c.coords(i[0])[0] - self.size_can[0] / 2, c.coords(i[0])[1] - self.size_can[1] / 2)
                    print(c.coords(i[0]))
                # for j in range(5):
                #     i.move()


        self.actm(act)

    def __create_Balls(self, c):
        for i in range(self.amount):
            x = randint(1, self.size_can[0] - 10)
            y = randint(1, self.size_can[1] - 10)
            self.balls.append([c.create_oval(x, y, x + 5, y + 5, fill=self.colors, outline="black"), x, y])

    def actm(self, anime):
        def actm_move():
            anime()
            root.after(self.interval, actm_move)

        return actm_move()


root = Tk()
powerOfResistance = Attraction(root)
powerOfResistance.attraction()
root.mainloop()