from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# screen properties
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("#343232")
screen.title("Snake Game")
screen.tracer(0)

# creating the objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# listening for keystrokes
screen.listen()
screen.onkey(snake.left, "a")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "d")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "w")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "s")
screen.onkey(snake.down, "Down")

game_running = True

while game_running:
    screen.update()
    # changes updates to a manageable speed
    time.sleep(0.1)
    snake.move()

    # detecting collision with food
    if snake.head.distance(food) < 20:
        food.relocate()
        snake.extend_snake()
        scoreboard.apple_eaten()
    
    # detecting collision with a wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    
    # detecting collision with tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


    
















screen.exitonclick()