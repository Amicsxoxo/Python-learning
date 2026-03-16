import tkinter

window = tkinter.Tk()
window.title("My First GUI Project")
window.minsize(width=500 , height= 300)

my_label = tkinter.Label(text= "I am a Label", font= ('Arial', 24, "bold"))
my_label.pack()

my_label["text"] = "New label"
my_label.config(text= "New label1")



window.mainloop()