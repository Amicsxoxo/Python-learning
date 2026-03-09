import random
from turtle import Turtle
 
COLORS = ["red" , "orange" , "yellow" , "blue" , "green" , "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("square")
    self.penup
    self.turtlesize(stretch_len= 2, stretch_wid= 1)
    self.setheading(180)
    self.xpos = 270
    self.ypos = 0
    
  def car_creation(self):
    
      colour = random.choice(COLORS)
      self.ypos = random.randint(-270,270)
      self.xpos = random.randint(240,270)
      self.color(colour)
      self.penup()
      self.goto(self.xpos, self.ypos)
  
  def car_move(self):
    self.car_creation()
    self.forward(STARTING_MOVE_DISTANCE)



