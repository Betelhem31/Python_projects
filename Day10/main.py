import os
from art import logo
os.system('cls')
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
from art import logo
print(logo)


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  num1 = float(input("What's the first number? "))
  for symbol in operations:
    print(symbol)
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation from th eline above: ")
    num2 = float(input("What's the next number? "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1}  {operation_symbol} {num2} = {answer}")


    if input(f"type 'y' to continue with {answer} or wanna start a new clalcualtion press 'n'") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

#recurssion
calculator()
