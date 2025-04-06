from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
r_score = Score((180,240))
l_score = Score((-180, 240))

r_paddle = Paddle((370, 0))

l_paddle = Paddle((-370, 0))
ball = Ball()
ball.penup()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # detect collision with the r_paddle
    if ball.xcor() > 360 and ball.distance(r_paddle) < 50 :
        ball.bounce_p()
    # detect collision with the l_paddle
    if ball.xcor() < -360 and ball.distance(l_paddle) < 50 :
        ball.bounce_p()
# detect if the r_paddle missed the ball
    if ball.xcor() > 390:
        ball.restart()
        l_score.score_increase()


    # detect if the l_paddle missed the ball
    if ball.xcor() < -390:
        ball.restart()
        r_score.score_increase()

screen.exitonclick()