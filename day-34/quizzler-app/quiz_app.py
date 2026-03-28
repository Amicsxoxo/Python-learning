from quiz_app_question_model import Question
from quiz_app_data import question_data
from quiz_app_quiz_brain import QuizBrain 
from ui import QuizInterface

question_bank = []


for question in question_data:
  question_text = question["question"]
  question_answer = question["correct_answer"]
  new_question = Question(question_text, question_answer)
  question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#   quiz.next_question()

print(f"You've completed the quiz \nYour final score is {quiz.score}/{quiz.question_number} ")