from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scores import Scoreboard
import time

# screen specs
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

# paddles, ball, and scoreboard creation
paddle_right = Paddle(350, 0)
paddle_left = Paddle(-350, 0)
ball = Ball()
scores = Scoreboard()

# movement controls and listeners
screen.listen()
screen.onkeypress(paddle_right.go_up, "Up")
screen.onkeypress(paddle_right.go_down, "Down")
screen.onkeypress(paddle_left.go_up, "w")
screen.onkeypress(paddle_left.go_down, "s")

# while loop control
game_on = True

while game_on:
    time.sleep(0.004)
    screen.update()
    ball.move()

    # ball bounce on top or bottom edge
    # -285 looks closer to the edge than -290 for some reason
    if (ball.ycor() < -285) or (ball.ycor() > 290):
        ball.bounce_y()
    
    # ball bounce on paddles
    if (((ball.distance(paddle_right) < 50) and (ball.xcor() > 320)) or 
        ((ball.distance(paddle_left) < 50) and (ball.xcor() < -320))):
            ball.bounce_x()
    
    # point for right paddle
    # -390 looked better on my screen
    if (ball.xcor() < -390):
        scores.right_point()
        ball.reset()
    
    # point for left paddle
    if (ball.xcor() > 380):
        scores.left_point()
        ball.reset()

screen.exitonclick()