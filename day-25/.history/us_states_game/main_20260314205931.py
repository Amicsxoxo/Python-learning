import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

data = pandas.read_csv("us_states_game/50_states.csv")

image = "us_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = (screen.textinput(title= "Guess a State!" ,prompt= "Whats another states nane? ")).title()
print(answer_state)

for answer_state in data:
  print("answer_state")

screen.mainloop()