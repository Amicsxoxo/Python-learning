from turtle import Turtle, Screen
from paddle import Paddle


screen = Screen()
screen.setup(width=800, height= 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()


screen.listen()

screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")
# tim = Turtle()

# tim.pencolor("white")
# tim.penup()
# tim.goto(0,-400)
# tim.setheading(90)
# tim.pensize(5)



# while tim.ycor() < 300:
#   tim.pendown()
#   tim.forward(10)
#   tim.penup()
#   tim.forward(10)
game_is_on = True
while game_is_on:
  screen.update()


screen.exitonclick()