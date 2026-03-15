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


data_1 = data.to_dict("list")
states_data = data_1["state"]
x_data = data_1["x"]
y_data = data_1["y"]

while counter() != 50:
  answer_state = (screen.textinput(title= f"{counter()}/50 Guess a State!" ,prompt= "Whats another states nane? ")).title()

  if answer_state == "Exit":
    break

  if answer_state in states_data:
    location = states_data.index(answer_state)
    xcor = x_data[location]
    ycor =y_data[location]
    tim.goto(xcor,ycor)
    if answer_state not in states_gotten:
      tim.write( arg=answer_state ,align= "center" , font= ("Arial", 8, "normal"))
      states_gotten.append(answer_state)
    
missed_states = []
for state in states_gotten:
  if state in states_data:
    states_data.remove(state)

stat
missed_states = pandas.DataFrame(states_data)
missed_states.to_csv("New_file")


screen.exitonclick()