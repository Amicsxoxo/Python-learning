def add(*arg):
  answer = 0
  for num in arg:
    answer += num
  return answer 
  
print(add(3,4,5,3,4))


class Car():

  def __init__(self, **kw):
    self.model = kw.get("model")
    self.make = kw.get("make")


my_car = Car(make = "Nissan")