from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

x = 10
def move_forward():
  tim.forward(10)

def move_backward():
  tim.backward(10)

def counterclockwise():
  tim.left(x)

def clockwise():
  tim.right(x)

def clear_screen():
  tim.reset()

#W= forward, S= backward, A =counterclockwise, D = Clockwise, C = cleardrawing


screen.listen()

screen.onkey(key= "w", fun = move_forward)

screen.onkey(key="s",fun= move_backward)

screen.onkey(key="a",fun= counterclockwise)

screen.onkey(key="d",fun=clockwise)

screen.onkey(key= "c", fun= clear_screen)

screen.exitonclick()