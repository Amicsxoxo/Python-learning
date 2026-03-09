from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height= 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-375,0))
r_paddle = Paddle((375,0))

ball = Ball()

scoreboard = Scoreboard()


screen.listen()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

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
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
    ball.bounce_x()
   
  


  if ball.xcor() > 400:
    ball.reset_position()
    scoreboard.l_point()
    sleep_time = 0.1

  if ball.xcor() < -400:
    ball.reset_position()
    scoreboard.r_point()
    sleep_time = 0.1

screen.exitonclick()