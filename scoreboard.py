FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 265)
        self.update_score()




    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)


    def level_up(self):
        self.score += 1
        self.update_score()


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER:", align="center", font=FONT)

