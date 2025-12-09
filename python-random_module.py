import random
import my_module

random_integer = random.randint(1,10)
print(random_integer)

print(my_module.pi)

random_float = random.random()
print(random_float)


random_decimal = (random.randint(0,5000))/1000
print(random_decimal)


random_decimal_2 = (random_float*5)
print(random_decimal_2)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")
