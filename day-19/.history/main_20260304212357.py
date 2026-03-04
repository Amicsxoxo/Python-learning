from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
  tim.forward(30)

def move_backward():
  tim.backward(30)

def counterclockwise():
  x -= 10
  tim.setheading(x)

def clockwise():
  x += 10
  tim.setheading(x)

#W= forward, S= backward, A =counterclockwise, D = Clockwise, C = cleardrawing


screen.listen()
screen.onkey(key= "w", fun = move_forward)

screen.onkey(key="s",fun= move_backwar)
screen.onkey(key=,fun=)
screen.onkey(key=,fun=)
screen.exitonclick()