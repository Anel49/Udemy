from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.x_move = 1
        self.y_move = 1
    
    # moves the ball
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    # inverts the y axis direction if bounced off the top or bottom edge
    def bounce_y(self):
        self.y_move *= -1
    
    # inverts the x axis direction since the ball bounced off a paddle
    def bounce_x(self):
        self.x_move *= -1
    
    # resets position of ball
    def reset(self):
        self.goto(0, 0)        
        self.bounce_x()

