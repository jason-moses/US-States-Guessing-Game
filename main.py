import turtle
import pandas
import csv
from tkinter import messagebox

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.tracer(0)
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

messagebox.showinfo("Rules", "Guess as many U.S. States as you can!\n Type 'exit' once you are done")

while len(guessed_states) < len(all_states):
    screen.update()
    answer_state = screen.textinput(f"{len(guessed_states)}/{len(all_states)} "
                                    f"States Guessed",
                                    "Enter the name of a U.S. State").title()

    if answer_state in all_states:
        timmy = turtle.Turtle()
        timmy.hideturtle()
        timmy.penup()
        state_data = data[data.state == answer_state]
        timmy.goto(state_data.x.item(), state_data.y.item())
        timmy.write(state_data.state.item())
        guessed_states.append(state_data.state.item())

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
                tom = turtle.Turtle()
                tom.hideturtle()
                tom.penup()
                tom.color("red")
                missing_state = data[data.state == state]
                tom.goto(missing_state.x.item(), missing_state.y.item())
                tom.write(missing_state.state.item())

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States to Revise.csv")
        with open("States to Revise.csv", newline='', encoding= 'utf-8') as csvfile:
            reader = csv.reader(csvfile)
            lines = ["\t".join(row) for row in reader]
            lines[0] = ""
            csv_text = "\n".join(lines)

        messagebox.showinfo("States to Revise", csv_text)
        break

screen.exitonclick()