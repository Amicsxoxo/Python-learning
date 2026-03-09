import time
from turtle import Screen
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height= 600)
screen.tracer(0)

carmanger = CarManager()
  carmanger.car_creation()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()


screen.exitonclick()