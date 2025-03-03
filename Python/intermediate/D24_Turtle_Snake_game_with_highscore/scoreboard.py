from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode="r") as high_score_file:
            self.high_score = int(high_score_file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

        
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as high_score_file:
                high_score_file.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def apple_eaten(self):
        self.score += 1
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-275, 255)
        self.write(f"Apples eaten: {self.score}", align="left", font=("Courier", 20, "normal"))
        self.goto(275, 255)
        self.write(f"High Score: {self.high_score}", align="right", font=("Courier", 20, "normal"))
    
  