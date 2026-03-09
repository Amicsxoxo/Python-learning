from turtle import Turtle

FONT = ("Arial" , 24 , "normal")


class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.goto(-230,240)
    self.score = 
    self.write(f"Level: 2" ,align= "center" , font= FONT)
