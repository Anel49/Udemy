from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.seth(90)   

    # resets turtle position to starting line
    def reset_position(self):
        self.goto(STARTING_POSITION)

    # move forward and backward
    def move_forward(self):
        self.seth(90)
        self.forward(MOVE_DISTANCE)    
    def move_backward(self):
        self.seth(270)
        self.forward(MOVE_DISTANCE)
