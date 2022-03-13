#Assignment even and odd

Number = int(input("Enter your number: "))
if Number % 2 == 0: # % is for remainder
    print("Even")
else:
    print("Odd")

#Assignment FizzBuzz
Number = int(input("Enter your number: "))

if Number % 3 == 0 and Number % 5 == 0:
    print("FizzBuzz")
elif Number % 3 == 0:
    print("Fizz")
elif Number % 5 == 0:
    print("Buzz")
else:
    print("Not Applicable")

#Assignment Calculator

def addition(operation):
    result = first_number + second_number
    print(result)
def subtraction(operation):
    result = first_number - second_number
    print(result)
def multiplication(operation):
    result = first_number * second_number
    print(result)
def division(operation):
    result = first_number / second_number
    print(result)

 
first_number = float(input("Enter your first number: "))
operation = str(input("Enter the math operation(+,-,*,/): "))
second_number = float(input("Enter your second number: "))

if operation == "+":
    addition(operation)
elif operation == "-":
    subtraction(operation)
elif operation == "*":
    multiplication(operation)
elif operation == "/":
    division(operation)
else:
    print("Invalid")