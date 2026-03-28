from tkinter import *
import requests

def get_quote():
    #Write your code here.
    #gets the json as an object
    quote = requests.get(url="https://api.kanye.rest")
    #Raises any error
    quote.raise_for_status()
    #Converts the object to a json file
    quotes = quote.json()
    #Finds the quote in the json file
    kayne_quote = quotes["quote"]
    #Writes the quote on the screen
    canvas.itemconfig(quote_text, text = f"{kayne_quote}")
    

    
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="day-33/Kayne-quote/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Welcome to Kanye Quotes!", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="day-33/Kayne-quote/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()