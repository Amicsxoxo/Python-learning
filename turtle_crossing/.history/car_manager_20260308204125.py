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
    self.xpos = -270
    self
    

  def num_of_cars(self):
    random.randint()


