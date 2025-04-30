# Write your solution here
number1 = int(input("Please input the first number: "))
number2 = int(input("Please input the second number: "))
operation = (input("Please input the operation (add, multiply or subtract): "))
if operation == "add":
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")
if operation == "multiply":
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")
if operation == "subtract":
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")
