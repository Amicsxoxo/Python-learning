from turtle import Turtle

FONT = ("Arial" , 24 , "normal")


class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.goto(-240,240)
    self.write(f"Level: " ,align= "center" , font= FONT)
