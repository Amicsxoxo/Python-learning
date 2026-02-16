import math

test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5


def paint_calc(height, width, cover):

  paint_area = height * width
  paint_cans = math.ceil(paint_area / cover)

  print(f"\nYou'll need {paint_cans} cans of paint")

paint_calc(height = test_h, width = test_w, cover = coverage)