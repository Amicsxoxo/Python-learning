student_height = input("Input a list of student heights: ").split()
for n in range(0, len(student_height)):
  student_height[n] = int(student_height[n])
print(student_height)


no_students = 0
total_height = 0
for numb in student_height:
  # total_height = total_height + numb
  total_height += numb
  no_students += 1


# no_students = 0
# for students in student_height:
#   no_students += 1
# print(no_students)

avg_height = round(total_height/no_students)
print(avg_height) 




