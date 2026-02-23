# def my_function():
#   for i in range(1,21):
#     if i == 20:
#       print("You got it")

# my_function()

# from random import randint

# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# dice_numb = randint(0,5)
# print(dice_imgs[dice_numb])


# year = int(input("What's your date of birth? "))
# if year > 1980 and year <= 1994:
#   print("Your are a millenial")
# elif year > 1994:
#   print("Your are gen z")

# age = int(input("What is your age? "))
# if age > 18:
#   print(f"You can drive at age. {age}")



# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = word_per_page * pages
# print(total_words)


def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)
  
mutate([1,2,3,5,8,13])