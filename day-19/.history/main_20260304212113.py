from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
  tim.forward(30)

def move_backward():
  tim.backward(30)

  

#W= forward, S= backward, A =counterclockwise, D = Clockwise, C = cleardrawing


screen.listen()
screen.onkey(key= "space", fun = move_forward)
screen.exitonclick()