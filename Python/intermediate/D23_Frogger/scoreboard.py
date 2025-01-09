from turtle import Turtle

FONT = ("Courier", 18, "bold")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.scoreboard_refresh()

    # clears and refreshes the scoreboard with updated level
    def scoreboard_refresh(self):
        self.clear()
        self.goto(-280, 260)
        self.write("Level: {}".format(self.level), align="left", font=FONT)
    
    # adds a level and refreshes the scoreboard with new level
    def update_level(self):
        self.level += 1
        self.scoreboard_refresh()
    
    # writes "GAME OVER" in the middle of the screen
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)