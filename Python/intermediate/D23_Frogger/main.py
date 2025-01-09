import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# listening for keyboard movements from player
screen.listen()
screen.onkeypress(player.move_forward, "w")
screen.onkeypress(player.move_forward, "Up")
screen.onkeypress(player.move_backward, "s")
screen.onkeypress(player.move_backward, "Down")

# while loop control
game_is_on = True

while game_is_on:
    time.sleep(0.005)
    screen.update()

    # creates a car and moves all cars for every tick
    car_manager.create_car()
    car_manager.move()
  
    # player made it to the other side; increase level and car speed
    if player.ycor() >= 290:
        car_manager.increase_speed()
        scoreboard.update_level()        
        player.reset_position()
    
    # collision with a car; game over
    for car in car_manager.cars:
        if player.distance(car) < 15:            
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()