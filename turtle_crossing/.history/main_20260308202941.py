import time
from turtle import Screen
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height= 600)
screen.tracer(0)


scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()


screen