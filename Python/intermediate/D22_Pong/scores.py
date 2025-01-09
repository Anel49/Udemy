from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        # initializes the scoreboard
        self.update_scores()
    
    # refresh scoreboard
    def update_scores(self):
        self.clear()
        self.goto(100, 180)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))
        self.goto(-100, 180)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))

    # right paddle gets a point; increment and update
    def right_point(self):
        self.right_score += 1
        self.update_scores()
    # left paddle gets a point; increment and update
    def left_point(self):
        self.left_score += 1
        self.update_scores()