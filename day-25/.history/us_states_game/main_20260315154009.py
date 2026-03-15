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
states_gotten = []
def counter():
  return len(states_gotten)


answer_state = ""
answer_state = (screen.textinput(title= "Guess a State!" ,prompt= "Whats another states nane? ")).title()


data_1 = data.to_dict("list")
states_data = data_1["state"]
x_data = data_1["x"]
y_data = data_1["y"]

game_on = True
while game_on:
  if answer_state in states_data:
    location = states_data.index(answer_state)
    xcor = x_data[location]
    ycor =y_data[location]
    tim.goto(xcor,ycor)
    states_gotten.append(answer_state)
    if answer_state not in states_gotten:
      tim.write( arg=answer_state ,align= "center" , font= ("Arial", 8, "normal"))
    answer_state = (screen.textinput(title= f"{c}Guess a State!" ,prompt= "Whats another states nane? ")).title()
  else:
    pass


screen.exitonclick()