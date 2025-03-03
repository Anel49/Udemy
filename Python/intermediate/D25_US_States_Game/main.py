import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Guessing Game")
# screen background
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# reading and creating list from CSV file
state_df = pandas.read_csv("50_states.csv")
state_ns = state_df.state.to_list()
# empty list for the guessed states
guessed_states = []

while len(guessed_states) < 50:
    answer = (screen.textinput(title=f"{len(guessed_states)}/50 States Guessed",
                               prompt="Guess a State")).title()

    # additionally checking if the state isn't already in the list to prevent
    # troublesome duplicates
    if (answer not in guessed_states) and (answer in state_ns):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # assigning variable to the row with a correct state name
        answer_data = state_df[state_df.state == answer]
        t.goto(answer_data.x.item(), answer_data.y.item())
        t.write(answer)
        # populating list with correct answer
        guessed_states.append(answer)
    
    # if the user wants to exit, make list and then CSV file of unanswered 
    # states and break out of the while loop to end the program
    if answer == "Exit":
        missing_states = []
        for state in state_ns:
            if state not in guessed_states:
                missing_states.append(state)
        missing_states_df = pandas.DataFrame(missing_states)
        missing_states_df.to_csv("states_to_learn.csv")
        break

screen.exitonclick()