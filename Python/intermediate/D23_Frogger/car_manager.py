from turtle import Turtle
import random

# the basic Tesla colors (Midnight Silver, Deep Blue Metallic, Solid Black, 
# and Ultra Red) excluding Pearl White because it wouldn't show up on the 
# white background and my favorite legacy colors (Titanium Silver, 
# Sequoia Green, and Anza Brown)
COLORS = ["#4B4F54", "#2B3289", "#191919", "#991821", "#645E58", "#364743", "#50473F"]
MOVE_SPEED = 1
MOVE_INCREMENT = 0.5


class CarManager(Turtle):

    def __init__(self):
        self.cars = []
        self.speed = MOVE_SPEED
    
    # creates a car
    def create_car(self):
        if random.randint(1, 48) == 1:
            car = Turtle("square")        
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            # facing west
            car.seth(180)
            car.color(random.choice(COLORS))
            car.goto(310, (random.randint(-250, 250)))
            self.cars.append(car)    

    # moves forward
    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    # increases speed of car
    def increase_speed(self):
        self.speed += MOVE_INCREMENT
    
    

