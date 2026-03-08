from turtle import Turtle

class Paddle(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.shapesize(stretch_wid=5, stretch_len= 1)
    self.penup()
    self.ypos = 0
    self.xcor = 375
    self.goto(self.xcor,self.ypos)

  def move_up(self):
    self.ypos += 10
    self.goto(self.xcor, self.ypos)
  def move_down(self):
    self.ypos -= 10
    self.goto(self.xcor,self.ypos)


  

