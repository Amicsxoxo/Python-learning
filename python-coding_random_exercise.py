import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)


randomInteger = random.randint(1,1000)

if randomInteger >= 500:
  print("Heads")
else:
  print("Tails")

# random.seed(321)

# randomInteger = random.randint(1,10)
# print(randomInteger)

# randomFloat = random.random() * 5
# print(randomFloat)