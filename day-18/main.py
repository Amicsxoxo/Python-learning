from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("classic")
tim.color("green")

# for square in range(4):
#   tim.forward(100)
#   tim.right(90)
# for dash in range(20):
#   tim.pencolor("green")
#   tim.forward(10)
#   tim.pencolor("white")
#   tim.forward(5)

r = 0
g = 0
b = 0

def color():
  r = random.random()
  g = random.random()
  b = random.random()
  colour = (r,g,b)
  return colour


at_home = True
heading = 0
tim.speed(0)

while at_home:
  tim.color(color())
  tim.circle(100)
  heading += 5
  tim.setheading(heading)

  if tim.heading() == 0.0:
    at_home = False

# positions = [0,90,180,270]
# tim.pensize(10)
# tim.speed(0)

# while True:
#   color()
#   tim.forward(20)
#   tim.setheading(random.choice(positions))


# number = 3
# for shapes in range(8):
#   color()
#   for corners in range(number):
#     tim.forward(100)
#     tim.right(360/number)
#   number += 1





















screen = Screen()
screen.exitonclick()