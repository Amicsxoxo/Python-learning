student_scores = input("Input your a list of student scores: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# max_score = student_scores[0]
# no_students = 0

# for n in student_scores:
#   no_students += 1
#   if n > student_scores[no_students -2]:
#     max_score = n
#   else:
#     max_score = student_scores[0]

# print(max_score)


highest_score = 0

for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")