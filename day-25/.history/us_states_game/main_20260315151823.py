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

answer_state = ""
answer_state = (screen.textinput(title= "Guess a State!" ,prompt= "Whats another states nane? ")).title()


data_1 = data.to_dict("list")
print(data_1)
states_data = data_1["state"]
location = states_data.index(answer_state)
print
# for answer_state in data_1["state"]:
#   print((data_1["state"]))
# for answer_state in data:


#   print(xcor, ycor)
#   tim.goto(xcor,ycor)
#   tim.write( arg=answer_state ,align= "center" , font= ("Arial", 8, "normal")) 

# screen.exitonclick()