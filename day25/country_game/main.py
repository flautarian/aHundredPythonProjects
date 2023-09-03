import os
import turtle 
import pandas

# US States Guess Game

screen = turtle.Screen()

script_dir = os.path.dirname(__file__)

screen.title("U.S States Game!")
img = script_dir +"/blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

csv_data = pandas.read_csv(script_dir + "/50_states.csv")

csv_data["guessed"] = False
turtle_states = []

game_state = True
while game_state or len(turtle_states) >= 50:
    titleguess = "Guess the state"
    if len(turtle_states) > 0:
        titleguess = f"{len(turtle_states)} States Correct!"
        
    answer_state = str(screen.textinput(title=titleguess, prompt="What states are left?")).lower().title()
    
    if answer_state == "None":
        game_state = False
    else:
        answer_case = csv_data[csv_data["state"] == answer_state]
        if len(answer_case) > 0:
            csv_data.loc[csv_data['state'] == answer_state, 'guessed'] = True
            answer_case["guessed"] = True
            new_state = turtle.Turtle()
            new_state.speed("fastest")
            new_state.penup()
            new_state.goto((answer_case.values[0][1], answer_case.values[0][2]))
            new_state.write(arg=answer_case["state"], move=False, align='left', font=('Arial', 8, 'normal'))
            turtle_states.append(new_state)

if len(turtle_states) >= 50:
    new_state = turtle.Turtle()
    new_state.speed("fastest")
    new_state.penup()
    new_state.goto((0, 0))
    new_state.write(arg="YOU WON!!, YOU ARE THE MASTER OF USA!", move=False, align='center', font=('Arial', 8, 'normal'))

#csv_data.to_csv(script_dir + "/50_states_mod.csv")

screen.exitonclick()
