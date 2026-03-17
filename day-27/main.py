from tkinter import *


def button_clicked():
  my_label.config(text= input.get())
  print("Button clicked")

window = Tk()
window.title("My First GUI Project")
window.minsize(width=500 , height= 300)
window.config(padx= 20, pady= 20)

#Label
my_label = Label(text= "I am a Label", font= ('Arial', 24, "bold"))
my_label["text"] = "New label"
my_label.grid(row= 0, column= 0)

#Button
button = Button(text="Pick me" ,command= button_clicked)
button.grid(row=1,column=1)

#Button 2
button_2 = Button(text="Pick me" ,command= button_clicked)
button_2.grid(row=0,column=2)

#Entry
input = Entry(width= 10)
input.grid(row=2, column= 3)


window.mainloop()