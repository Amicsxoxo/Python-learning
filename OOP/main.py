#Learning Object Oriented Programming


#Named the class using CamelCase
class Dog:
  def __init__(self,name):
    self.name = name
    print(name)
  #Created a method that adds one to the value
  def add_one(self,x):
    return x + 1
  
  #Created a method for the class
  def bark(self):
    #What the method does when being called
    print('Bark')
    
#Created an object from the class
d = Dog()

print(d.add_one(3))

#Used the method bark
d.bark()

#Checked the type
print(type(d))
