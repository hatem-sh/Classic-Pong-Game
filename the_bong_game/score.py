from turtle import Turtle

class Score(Turtle):
    def __init__(self,position):

        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(position)
        self.color("white")
        self.penup()
        self.write(self.score,False,align="left", font=("Arial", 40, "normal"))


    def score_increase(self):
        self.clear()
        self.score += 1
        self.write(self.score,False,align="left", font=("Arial", 40, "normal"))
