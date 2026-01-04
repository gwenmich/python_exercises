import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_count = 0

data = pandas.read_csv("50_states.csv")

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{correct_count}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in data["state"].values:
        guessed_states.append(answer_state)
        state_data = data[data["state"] == answer_state]
        x = state_data["x"].item()
        y = state_data["y"].item()
        pen.goto(x, y)
        pen.write(answer_state)
        correct_count += 1










