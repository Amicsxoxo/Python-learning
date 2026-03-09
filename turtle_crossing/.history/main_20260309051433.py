import time
from turtle import Screen
from scoreboard import Scoreboard
from car_manager import CarManager
from player import Player,FINISH_LINE_Y
import random

screen = Screen()
screen.setup(width=600, height= 600)
screen.tracer(0)

carmanger = CarManager()
scoreboard = Scoreboard()
player = Player()

game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()
  for _ in range(random.randint(1,12)):
    carmanger.car_creation


  screen.listen()
  screen.onkey(player.move_up , "Up")
  screen.onkey(player.move_down , "Down")




  if player.ycor() > FINISH_LINE_Y:
    scoreboard.update()
    player.restart()



screen.exitonclick()

