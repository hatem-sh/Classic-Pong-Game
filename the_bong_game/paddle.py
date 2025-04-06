from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 40
        # Check if new_y exceeds the top boundary (screen height is 600, paddle height is 100)
        if new_y < 250:  # 300 (half screen) - 50 (half paddle height) = 250
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 40
        # Check if new_y exceeds the bottom boundary
        if new_y > -250:  # -300 (half screen) + 50 (half paddle height) = -250
            self.goto(self.xcor(), new_y)
