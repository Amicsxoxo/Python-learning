from tkinter import *

window = Tk()
window.title("My First GUI Project")
window.minsize(width=500 , height= 300)

my_label = Label(text= "I am a Label", font= ('Arial', 24, "bold"))
my_label.pack()

my_label["text"] = "New label"
my_label.config(text= "New label_2")


def button_clicked():
  my_label.config(text= input.get())
  print("Button clicked")


#Button
button = Button(text="Pick me" ,command= button_clicked)
button.pack()

#Entry
input = Entry(width= 10)
input.pack()


window.mainloop()