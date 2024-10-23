# drawing basic shapes using turtle graphics

from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
screen = Screen()

# positioning
t.color("black")
t.penup()
t.goto(-37, 234)
t.pendown()

# task 1: draw a square
for i in range(4):
    t.forward(68)
    t.right(90)

# positioning
t.penup()
t.goto(-78, 234)
t.pendown()

# task 2: draw a triangle
t.color("red")
for i in range(3):
    t.forward(150)
    t.right(120)

# task 3: draw a larger square
t.color("orange")
for i in range(4):
    t.forward(150)
    t.right(90)

# task 4: draw a pentagon
t.color("gold")
for i in range(5):
    t.forward(150)
    t.right(72)

# task 5: draw a hexagon
t.color("green")
for i in range(6):
    t.forward(150)
    t.right(60)

# task 6: draw a heptagon
t.color("blue")
for i in range(7):
    t.forward(150)
    # precision matters
    t.right(51.428571428571428571428571428571428571428571428571)

# task 7: draw a octogon
t.color("purple")
for i in range(8):
    t.forward(150)
    t.right(45)

# task 8: draw a nonagon
t.color("brown")
for i in range(9):
    t.forward(150)
    t.right(40)

# task 9: draw a decagon
t.color("gray")
for i in range(10):
    t.forward(150)
    t.right(36)

# positioning
t.color("black")
t.penup()
t.goto(-3, 234)
t.right(90)
t.pendown()

# task 10: draw a dashed line
for i in range (23):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

# keeping the screen from automatically closing
screen.exitonclick()