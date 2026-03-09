from turtle import Turtle

FONT = ("Arial" , 24 , "normal")


class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.goto(-230,240)
    self.score = 0
    self.write(f"Level: {self.score}" ,align= "center" , font= FONT)
