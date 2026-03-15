with open(file= "day-26/Exercise_3/file1.txt") as file1:
  file_1 = file1.readlines()
with open(file= "day-26/Exercise_3/file2.txt") as file2:
  file_2 = file2.readlines()

result = [int(num) for num in file_1 if num in file_2]

print(result)