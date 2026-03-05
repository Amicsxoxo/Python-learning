from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width= 500, height= 400)

is_race_on = False

user_bet = screen.textinput(title= "Make a bet" , prompt= "Which turtle will win the race? Enter a color: ")
print(user_bet)

colors = ["red", "blue", "yellow", "orange", "purple", "green"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
  tim = Turtle(shape= "turtle")
  tim.penup()
  tim.goto(x= -230, y= y_positions[turtle_index])
  tim.color(colors[turtle_index])
  all_turtles.append(tim)

if user_bet:
  is_race_on = True

while is_race_on:

  for turtle in all_turtles:
    if turtle.xcor() > 230:
      is_race_on = False
      winnng_color = turtle.pencolor()
      if winnng_color == user_bet:
        print(f"You've won! The {winnng_color} turtle is the winner")
      else:
        print(f"You've lost! The {winnng_color} turtle is the winner")

    rand_distance = random.randint(0,10)
    turtle.forward(rand_distance)

screen.exitonclick()