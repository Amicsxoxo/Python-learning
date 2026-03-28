# age : int
# name : str
# height : float
# is_human : bool


#Type hints is used to give hints on the type of variable to be inputted or outputted the ":" symbol is used to specify the type of data to be inputed while "->" is used to specify the type of data expected to be outputted its also shown in some documentation of class and parameters
def police_check(age : int) -> bool : #Type hints is being used here
  if age > 18:
    can_drive = True
  else:
    can_drive = False
  return can_drive

print(police_check(12))
if police_check():
  print("You can drive")
else:
  print("You cannot drive")