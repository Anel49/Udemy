from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
step = 30
degrees = 15
turtle.pensize(3)
turtle.shapesize(1.8)

def forward():
    turtle.forward(step)
def backward():
    turtle.backward(step)
def left():
    turtle.left(degrees)
def right():
    turtle.right(degrees)
def clear():
    # I could have done home() then clear(), but I think it looks better when
    # the drawing is erased before the turtle repositions itself.
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkey(forward, "w")
screen.onkey(forward, "Up")
screen.onkey(backward, "s")
screen.onkey(backward, "Down")
screen.onkey(left, "a")
screen.onkey(left, "Left")
screen.onkey(right, "d")
screen.onkey(right, "Right")

screen.onkey(clear, "c")

screen.exitonclick()