import turtle
import pandas


data = pandas.read_csv("us_states_game/50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")

tim = turtle.Turtle()
tim.penup()
tim.hideturtle()

image = "us_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


answer_state = (screen.textinput(title= "Guess a State!" ,prompt= "Whats another states nane? ")).title()



for answer_state in data:
  print("answer_state")
  xcor = data.answer_state.x
  ycor = data.answer_state.y

  tim.goto(xcor)

screen.mainloop()