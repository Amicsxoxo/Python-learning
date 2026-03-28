from tkinter import *
from quiz_app_quiz_brain import QuizBrain 

THEME_COLOR = "#375362"

#Creating a class
class QuizInterface:
  #intializing the class
  def __init__(self, quiz_brain : QuizBrain): #Add the QuizBrain module to ensure that the class of the passed in argument is the same class as the QuizBrain
    self.quiz = quiz_brain
    self.window = Tk()
    self.window.title("Quizzler")
    self.window.config(padx= 20, pady= 20, bg= THEME_COLOR)

    #Creates an image that can be used by the buttons
    good_button = PhotoImage(file="day-34/quizzler-app/images/true.png")
    bad_button = PhotoImage(file="day-34/quizzler-app/images/false.png")

    #Created the scoreboard
    self.scoreboard = Label(text="Score: 0", font=("Arial", 12, "bold"), fg="white", bg= THEME_COLOR, padx=20, pady=20)
    self.scoreboard.grid(row= 0, column= 1)

    #Created the canvas where the text will be displayed
    self.canvas = Canvas(height= 250, width= 300,bg = "white", highlightthickness= 0)
    self.quiz_text = self.canvas.create_text( 150, 125, width=280,  text= "Text",font= ("Arial", 20, "italic"), fill= THEME_COLOR)
    self.canvas.grid(row= 1, column=0,  columnspan= 2, pady= 50)

    #Created the correct button
    self.correct_button = Button(image= good_button, highlightthickness= 0, command= self.correct__button)
    self.correct_button.grid(row= 2, column= 0)
    self.correct_button.config( padx= 20, pady= 20 ,)

    #Created thewromg button
    self.wrong_button = Button(image= bad_button, highlightthickness= 0, command= self.wrong__button)
    self.wrong_button.grid(row= 2, column= 1)
    self.wrong_button.config( padx= 20, pady= 20 ,)


    self.get_next_question()
    #Keeps the screen running in an infinite loop
    self.window.mainloop()

  def get_next_question(self):
    #Changes the background to white
    self.canvas.config(bg="white")    #Checks if there are still questions
    if self.quiz.still_has_questions():
      #Assigns the next question to a variable
      q_text = self.quiz.next_question()
      #Updates the scoreboard as you change questions
      self.scoreboard.config(text= f"Score : {self.quiz.score}")
      #Configures the text on the canvas to show the next question in the list of questions
      self.canvas.itemconfig(self.quiz_text, text = q_text)
    else:
      #Tells the user they've reached the end of the questions
      self.canvas.itemconfig(self.quiz_text, text = "You've reached the end of the")
      self.correct_button.config(state="disabled")
      self.wrong_button.config(state="disabled")

  def correct__button(self):
    #Checks if the you hit the right button then checks if the answer is true
    is_right = self.quiz.check_answer(user_answer= "True")
    self.give_feedback(is_right)

  def wrong__button(self):
      #Checks if the you hit the wrong button then checks if the answer is false
    is_right = self.quiz.check_answer(user_answer= "False")
    self.give_feedback(is_right)

  def give_feedback(self, is_right):
    #Changes the background to green or red depending on if the user is correct or not 
    if is_right:
      self.canvas.config(bg="green")
    else:
      self.canvas.config(bg="red")
    #After a second changes the background back to white and displays the next question 
    self.window.after(1000, self.get_next_question)
