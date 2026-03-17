from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20 , pady= 20)


def calc():
  ans = round(float(input.get()) * 1.60934, 2)
  answer.config(text=f"{str(ans)}")


# empty = Label(text= " ", font= ('Arial', 12, "normal"))
# empty.grid(row= 0, column= 0)

input = Entry(width=10)
input.grid(row= 0, column= 1)

miles = Label(text= "Miles", font= ('Arial', 12, "normal"))
miles.grid(row= 0, column= 2)

is_equals = Label(text= "is equal to", font= ('Arial', 12, "normal"))
is_equals.grid(row= 1, column= 0)


answer = Label(text= "0", font= ('Arial', 12, "normal"), justify= "center")
answer.grid(row= 1, column= 1)

km = Label(text= "Km", font= ('Arial', 12, "normal"), justify= "center")
km.grid(row= 1, column= 2)


calculate = Button(text= "Calculate" , command= calc)
calculate.grid(row= 2, column= 1)


window.mainloop()