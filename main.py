import time
from turtle import  Turtle
from turtle import Screen

from paddle import Paddle
from ball import  Ball
from Scorecard import Scorecard

score = 0

screen = Screen()
screen.title("PONG GAME")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)


paddle_left = Paddle((-370, 0))
paddle_right = Paddle((370, 0))
ball = Ball()
#scorecard = Scorecard()


screen.listen()
screen.onkeypress(paddle_left.go_up, "w")
screen.onkeypress(paddle_left.go_down, "s")
screen.onkeypress(paddle_right.go_up, "o")
screen.onkeypress(paddle_right.go_down, "l")


while True:
    screen.update()

    ball.move()
    # collision with walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    # collision with paddle
    if ball.distance(paddle_left) < 50:
        ball.paddle_collision()
        score = score + 1

    if ball.distance(paddle_right) < 50:
        ball.paddle_collision()
        score = score + 1

    # game termination
    if ball.xcor() >= 400 or ball.xcor() <= -400:
        break




    time.sleep(0.05)


print(f"score is {score}")



screen.exitonclick()