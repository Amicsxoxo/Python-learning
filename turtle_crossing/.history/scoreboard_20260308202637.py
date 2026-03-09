from turtle import Turtle

FONT = ("Courier" , 24 , "normal")


class Scoreboard(Turtle):
  def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
    super().__init__()