import time
import json
import datetime as dt


loop = True 


while loop:
  try :
    with open("task_cli/data.json", mode= "r") as file:
      data = json.load(file)
  except json.decoder.JSONDecodeError: 
    data = {}


  users_input = input("task_cli ")

  input_list = users_input.split()

  #Add tasks
  if input_list[0].lower() == "add":
    status = "todo"
    createdAt = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updatedAt = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    description = ""
    for  _ in input_list[1:]:
      description +=  (_.strip("'") + " ")

    new_task = {
        "status" : status,
        "createdAt" : createdAt,
        "updatedAt" : updatedAt, 
        "description" : description
      }
    if len(data) > 0:
      all_keys = []
      for keys, values  in data.items():
        all_keys += str(keys)
        new_key = int(max(all_keys)) + 1
    else:
      new_key = 1
    data[new_key] = new_task

    with open("task_cli/data.json", mode= "w") as file:
      json.dump(data, file, indent= 4)
    print(f"Task added Successfully (ID: {new_key})")

  #Update tasks
  elif input_list[0].lower() == "update":

    if len(input_list) <= 3:
      print("Pls use this format:  task-cli update 1 'Buy groceries and cook dinner'")

    else:
      updated_description = ""
      for _ in input_list[2:]:
        updated_description += (_.strip("'")+ " ")
      data[input_list[1]]["description"] = updated_description

      data[input_list[1]]["updatedAt"] = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      with open("task_cli/data.json", mode= "w") as file:
        json.dump(data, file, indent= 4)
      print(f"Task ID : {input_list[1]} updated")

  #Delete tasks
  elif input_list[0].lower() == "delete":

    data.pop(input_list[1], None)
    with open("task_cli/data.json", mode= "w") as file:
      json.dump(data, file, indent= 4)
    print("Task Deleted")

  #Change status to done
  elif input_list[0].split("-")[-1].lower() == "done":

    data[input_list[1]]["status"] = "done"
    with open("task_cli/data.json", mode= "w") as file:
      json.dump(data, file, indent= 4)
    print(f"Task ID {input_list[1]} status updated to Done")

  #Change status to in progress
  elif input_list[0].split("-")[-1].lower() == "progress":

    data[input_list[1]]["status"] = "in-progress"
    with open("task_cli/data.json", mode= "w") as file:
      json.dump(data, file, indent= 4)
    print(f"Task ID {input_list[1]} status updated to In-Progress")

  #Print a list of tasks
  elif input_list[0].lower() == "list":
    if len(input_list) < 2:
      for keys, values in data.items():
        print(f"(ID :{keys}), {values["description"]}")

    else:
      for keys, values in data.items():
        if values["status"] == input_list[1]:
          print(f"{input_list[1]} Task (ID :{keys}), {values["description"]}")

  elif input_list[0].lower() == "cancel":
    loop = False

  else:
    print("Pls input a valid input")


  print("\n")
  time.sleep(.5)

