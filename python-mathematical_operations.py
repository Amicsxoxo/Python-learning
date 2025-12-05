# print(3*3+3/3-3)


height = input("What is your height in m: ")
weight = input("What is your weight in kg: ")

bmi = int(weight) / float(height) ** 2

bmi_as_int = int(bmi)
print(bmi_as_int)

# print(type(height))