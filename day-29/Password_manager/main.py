from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate__password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(choice(letters))
    password_list += [choice(letters) for char in range(randint(8, 10))]

    # for char in range(nr_symbols):
    #   password_list += choice(symbols)
    password_list += [choice(symbols) for char in range(randint(2, 4))]

    # for char in range(nr_numbers):
    #   password_list += choice(numbers)
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

  website = website_name.get()
  email = email_username_entry.get()
  password = password_entry.get()

  #A Dictionary in the json style
  new_data = {
    website :{
      "Email" : email,
      "Password" : password,
    }
  }

  if len(website) == 0 or len(email) == 0:
    messagebox.showinfo(title= "Oops", message= "Please don't leave any field empty")
  else:

    try:
      with open("day-29/Password_manager/data.json", mode= "r") as file:
        #Reading old data
        data = json.load(file)

    except FileNotFoundError:
      #Opening a new file and inserting data
      with open("day-29/Password_manager/data.json", mode= "w") as file:
        json.dump(new_data, file, indent= 4)

    else:
      #Updating old data with new data
      data.update(new_data)
      #Saving Updated data
      with open("day-29/Password_manager/data.json", mode= "w") as file:
        json.dump(data, file, indent= 4)

    finally:
      #Clears the password and website name entry box
      password_entry.delete(0,END)
      website_name.delete(0,END)

#-----------------------------REMOVE PASSWORD-------------------------- #


#-----------------------------SEARCH PASSWORD-------------------------- #
def find_password():
  website = website_name.get()
  
  try:
    with open("day-29/Password_manager/data.json", mode= "r") as file:
      data = json.load(file)

  except json.decoder.JSONDecodeError or FileNotFoundError:
    messagebox.showerror(title= "Error", message= "No Data file Found")

  else:
    if website in data:
        users_data = data[website]
        users_email = users_data["Email"]
        users_password = users_data["Password"]
        pyperclip.copy(users_password)
        messagebox.showinfo(title= website, message= f"Email: {users_email} \nPassword: {users_password}")
    else:
        messagebox.showinfo(title=website, message= "No details for this website exists. ")




#-----------------------------UI SETUP -------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx= 20, pady= 20)

#Creates a canvas or screen
canvas = Canvas(width= 200, height= 200 , highlightthickness= 0)
logo_image = PhotoImage(file="day-29/Password_manager/logo.png")
canvas.create_image(100,100, image = logo_image)
canvas.grid(row=0, column= 1)

website_label = Label(text="Website")
website_label.grid(row= 1, column= 0)

website_name = Entry(width= 35)
website_name.focus()
website_name.grid(row= 1, column= 1, columnspan= 2)

search_button = Button(text= "Search", width= 16, highlightthickness= 0, command= find_password)
search_button.grid(row= 1, column= 3)

email_username_label = Label(text= "Email/Username")
email_username_label.grid(row= 2, column= 0)

email_username_entry = Entry(width= 55)
email_username_entry.grid(row= 2, column= 1, columnspan= 3)
email_username_entry.insert(0, "onwukanjo@gmail.com")

password_label = Label(text= "Password")
password_label.grid(row= 3, column= 0)

password_entry = Entry(width= 35)
password_entry.grid(row= 3, column= 1,columnspan=2)

generate_password = Button(text= "Generate Password" , highlightthickness= 0, command= generate__password, width= 16)
generate_password.grid(row= 3, column= 3)

add_button = Button(text= "add",width= 47, highlightthickness=0, command= save)
add_button.grid(row= 4, column=1, columnspan= 3)



window.mainloop()