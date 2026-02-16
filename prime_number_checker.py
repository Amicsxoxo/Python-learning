def prime_checker(number):
  is_prime = True
  for i in range(2, number - 1):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number")
  else:
    print("It's not a prime number")



n = int(input("Check this number: "))
prime_checker(number=n)












# import math

# n = int(input("Check this number: "))


# def prime_checker(number):
#   checker = []
#   limit = int(math.sqrt(number))
#   if limit > 0:
#     for num in range(2,number):
#       checker.append(number % num)
#     if 0 in checker:
#       print("It's not prime number")
#     else:
#       print("It's a prime number")
#     print(checker)





# prime_checker(number=n)