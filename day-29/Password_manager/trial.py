import json

with open("day-29/Password_manager/data.json", mode= "r") as file:
  data = json.load(file)
  if "Amazon" in data:
    files = data["Amazon"]
    print(files["Email"])
  else:
    print("Bad job")