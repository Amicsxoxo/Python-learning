import random
import time


tim = time.time()
color_list = [ (199, 162, 100), (62, 91, 128), (140, 170, 192), (139, 90, 48), (219, 206, 119), (135, 27, 52), (32, 41, 67), (78, 16, 36), (149, 59, 85), (167, 154, 49), (187, 143, 162), (134, 183, 147), (46, 55, 100), (181, 95, 107), (56, 39, 27), (96, 118, 167), (80, 150, 159), (89, 152, 92), (71, 118, 93), (220, 175, 187), (169, 207, 163), (161, 202, 215), (192, 95, 74), (178, 187, 213), (46, 73, 75), (76, 69, 44)]

time.colormode(255)
time.speed(0)


def color_dots():
  color = random.choice(color_list)
  time.pendown()
  time.color(color)
  time.begin_fill()
  time.circle(10)
  time.end_fill()


time.penup()

x = -300
y = -300

time.goto(x, y)

for _ in range(10):
  y += 50
  time.goto(x,y)
  for _ in range(10):
    color_dots()
    time.penup()
    time.forward(50)






time.Screen().exitonclick()