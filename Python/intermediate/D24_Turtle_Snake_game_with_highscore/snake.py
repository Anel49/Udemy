from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# quick way to update step
STEP = 20

class Snake:
    def __init__(self):
        
        self.snake_segments = []

        # creates first three segments
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        
        # easier to identify the head this way
        self.head = self.snake_segments[0]

    # continuously moves the snake head and updates following segments
    def move(self):
        for segment in range(len(self.snake_segments)-1, 0, -1):
            location = (self.snake_segments[segment - 1].xcor(), self.snake_segments[segment - 1].ycor())
            self.snake_segments[segment].goto(location)

        self.snake_segments[0].forward(STEP)        

    # segment creation
    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake_segments.append(segment)
    
    # adds a segment to the end of the snake
    def extend_snake(self):
        self.add_segment(self.snake_segments[-1].position())
    
    def reset(self):
        for segment in self.snake_segments:
            segment.goto(1000, 1000)

        self.snake_segments.clear()
        
        # creates first three segments
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        
        # easier to identify the head this way
        self.head = self.snake_segments[0]
    
    # snake controls; won't let player turn back into snake body
    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)    
    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)
    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)