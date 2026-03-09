import random
from turtle import Turtle
from player import Player
 
COLORS = ["red" , "orange" , "yellow" , "blue" , "green" , "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
  def __init__(self):
    self.all_cars = []
    self.move = STARTING_MOVE_DISTANCE
    self.rand = 6
    
    
  def car_creation(self):
    rand_chance = random.randint(1,self.rand)
    if rand_chance == 1:
      new_car = Turtle()
      new_car.shape("square")
      new_car.penup()
      new_car.turtlesize(stretch_len= 2, stretch_wid= 1)
      new_car.color(random.choice(COLORS))    
      xpos = 300
      ypos = random.randint(-270,270)
      new_car.goto(xpos, ypos)
      self.all_cars.append(new_car)
      
  
  def car_move(self):
    for cars in self.all_cars:
      cars.setheading(180)
      cars.forward(self.move)

  def reset_car(self):
    for _ in self.all_cars:
      _.hideturtle()
    self.all_cars = []
    self.move = STARTING_MOVE_DISTANCE
    self.rand = 6

  def move_increase(self):
    self.move += MOVE_INCREMENT
    self.rand -= 1



