import time
from turtle import Screen
from scoreboard import Scoreboard
from car_manager import CarManager
from player import Player,FINISH_LINE_Y
import random

screen = Screen()
screen.setup(width=600, height= 600)
screen.tracer(0)

car_manger = CarManager()
scoreboard = Scoreboard()
player = Player()



game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()
  car_manger.car_creation()
  car_manger.car_move()


  for cars in car_manger.all_cars:
    if player.distance(cars) < 20:
      player.restart()
      car_manger.reset_car()
      scoreboard.restart()


  screen.listen()
  screen.onkey(player.move_up , "Up")
  screen.onkey(player.move_down , "Down")




  if player.ycor() > FINISH_LINE_Y:
    scoreboard.update()
    player.restart()
    car_manger.reset_car()
    car_manger.move_increase()

  
  
  


screen.exitonclick()

