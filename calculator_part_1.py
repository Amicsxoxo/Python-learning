from calculator_art import logo

def add(n1,n2):
  """To add two digits together"""
  return n1 + n2

def subtract(n1,n2):
  """To subtract a digit from another"""
  return n1 - n2

def multiply(n1,n2):
  """To multiply two digits togeter"""
  return n1 * n2

def divide(n1,n2):
  """To divide a digit by another"""
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}
def calculator():
  print(logo)
  num1 = float(input("What's the first number: "))
  for symbols in operations:
    print(symbols)
  option = True
  while option:
    operation_symbol = input("Pick an operation: ")

    num2 = float(input("What's the next number: "))

    calculation_symbol = operations[operation_symbol]
    answer = calculation_symbol(num1, num2)

    answer = calculation_symbol(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    continuation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ").lower()
    if continuation == 'y':
      option = True
      num1 = answer
    else:
      option = False
      calculator()

calculator()