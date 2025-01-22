import turtle
import pandas

FONT = ("Arial", 10, "normal")

screen = turtle.Screen()
screen.title("U.S State Quiz Game")
bg_image = "blank_states_img.gif"
screen.addshape(bg_image)
turtle.shape(bg_image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
# print(all_states)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        ## Use List Comprehension
        missing_states = [state for state in all_states if state not in guessed_states]

        missing_state_df = pandas.DataFrame(missing_states)
        missing_state_df.to_csv("state_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


screen.mainloop()

