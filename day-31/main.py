from tkinter import *
import pandas
import random

BACKGROUND_COLOUR = "#B1DDC6"
#Reads the csv data
try:
  words_data = pandas.read_csv("day-31/data/unknown_words.csv")
except FileNotFoundError:
  words_data = pandas.read_csv("day-31/data/french_words.csv")
finally:
  #converts the data to a dictionary nested in a list, each row is in a seprate dictionary in the list
  data_dict = words_data.to_dict(orient= "records")

#------------------------------------------ Data  ------------------------------------------------#

def next_card():
  global rand_data, flip_timer

  #cancels the flip
  window.after_cancel(flip_timer)
  rand_data = random.choice(data_dict)
  rand_french = rand_data["French"]
  canvas.itemconfig(card_title, text = f"French", fill = "black")
  canvas.itemconfig(card_word, text = f"{rand_french}", fill = "black")
  canvas.itemconfig(cavnvas_image, image = front_image)

  #Delays the window for 3secs then flips the card
  flip_timer =  window.after(3000, card_flip)

def card_flip():
  #Function to flip the card
  canvas.itemconfig(cavnvas_image, image = back_image)
  rand_english = rand_data["English"]
  canvas.itemconfig(card_title, text = f"English", fill = "white")
  canvas.itemconfig(card_word, text = f"{rand_english}", fill = "white")

def known_card():
  data_dict.remove(rand_data)
  next_card()


#------------------------------------------ UI ------------------------------------------------#

window = Tk()
window.title("Flashy")
window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOUR)

#The flipping timer it waits for 3secs
flip_timer =  window.after(3000, card_flip)


#Creates a canvas
canvas = Canvas(width= 800, height= 526, highlightthickness= 0, bg= BACKGROUND_COLOUR)
front_image = PhotoImage(file="day-31/images/card_front.png")
cavnvas_image = canvas.create_image(400,263, image= front_image)
canvas.grid(row=0, column=0, columnspan=2)
back_image = PhotoImage(file="day-31/images/card_back.png")


#Add text to the canvas after specifing thier x and y position
card_title = canvas.create_text(400,150, text= "", font= ("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text= "", font= ("Arial", 60, "bold"))



#Creating buttons
wrong_image = PhotoImage(file="day-31/images/wrong.png")
wrong_button = Button(image= wrong_image, highlightthickness= 0, padx= 50, command= next_card)
wrong_button.grid(row=1, column= 0)


right_image = PhotoImage(file="day-31/images/right.png")
right_button = Button(image= right_image, highlightthickness= 0, padx= 50, command= known_card)
right_button.grid(row=1,column=1)



next_card()

window.mainloop()

#Firsts converts the dictionary to a dataframe
data = pandas.DataFrame(data_dict)
#Converts the dataframe into a csv file and then saves it 
data.to_csv("day-31/data/unknown_words.csv", index= False)