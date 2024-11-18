import random
from turtle import Turtle, Screen
from tkinter import messagebox

# screen specs
screen = Screen()
screen.setup(width=960, height=810)
screen.bgcolor("#343232")

# list to put the turtles in
turtle_list = []

# preset turtle colors and coords
turtle_colors = ("#ffc09f", "#ffee6e", "#a0ced9", "#adf7b6")
turtle_y_coords = (153, 53, -47, -147)

# placing bet prompt
user_bet = screen.textinput(title="Place Your Bet",
    prompt="Which turtle will win? Salmon, yellow, cyan, or mint?").lower()

# turtle creation
for turtle_i in range(0, 4):
    turtle = Turtle(shape="turtle")
    turtle.pencolor(turtle_colors[turtle_i])
    turtle.fillcolor(turtle_colors[turtle_i])
    turtle.penup()
    turtle.goto(-400, turtle_y_coords[turtle_i])
    turtle_list.append(turtle)

race_on = False

# start the race if a bet was made
if user_bet:
    race_on = True

while race_on:
    for turtle in turtle_list:
        
        # first checks if any of the turtles have finished
        if turtle.xcor() > 460:
            # identifies winner color
            winner = turtle.pencolor()
            # switch case determines color string name
            match winner:
                case (1.0, 0.7529411764705882, 0.6235294117647059):
                    winner = "Salmon"
                case (1.0, 0.9333333333333333, 0.43137254901960786):
                    winner = "Yellow"
                case (0.6274509803921569, 0.807843137254902, 0.8509803921568627):
                    winner = "Cyan"
                case (0.6784313725490196, 0.9686274509803922, 0.7137254901960784):
                    winner = "Mint"
            
            # add to the end if the user won or not
            if user_bet == winner.lower():
                result = "Congratulations! You won!"
            else:
                result = "You lost!"

            # popup showing winner and if user won or not
            messagebox.showinfo(f"{winner} wins!", f"{result}")

            # end movement
            race_on = False
            # break out of loop so following code doesn't run
            break

        distance = random.randint(0, 10)
        turtle.forward(distance)        

screen.exitonclick()