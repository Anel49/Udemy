from turtle import Turtle
import random

FOOD_SIZE = 0.75

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(FOOD_SIZE, FOOD_SIZE)
        self.color("red")
        self.speed("fastest")
        self.relocate()
    
    def relocate(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))