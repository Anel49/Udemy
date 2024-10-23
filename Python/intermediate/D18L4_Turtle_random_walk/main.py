import turtle
from turtle import Screen
import random

# TASKS:
# speed the turtle up
# make its lines thicker
# randomize its color
# randomize its direction

t = turtle.Turtle()
screen = Screen()
turtle.colormode(255)
directions = [0, 90, 180, 270]

t.shape("circle")
t.speed("fastest")
t.pensize(15)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

while True:
    t.color(random_color())    
    t.forward(30)
    t.right(random.choice(directions))

screen.exitonclick()