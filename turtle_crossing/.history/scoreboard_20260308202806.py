from turtle import Turtle

FONT = ("Courier" , 24 , "normal")


class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.goto(-240,270)
    self.write("Level")