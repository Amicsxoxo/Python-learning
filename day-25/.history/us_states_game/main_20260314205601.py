import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "us_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = (screen.textinput(title= "Guess a State!" ,prompt= "Whats another states nane? ")).ti
print(answer_state)


screen.mainloop()