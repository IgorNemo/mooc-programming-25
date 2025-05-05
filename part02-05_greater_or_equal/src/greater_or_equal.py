# Write your solution here
number1 = int(input("Please print the first number: "))
number2 = int(input("Please print the second number: "))
if (number1 - number2) < 0:
    print(f"The greater number was: {number2}")
elif(number1 - number2) > 0:
    print(f"The greater number was: {number1}")
else:
    print(f"The numbers are equal!")
    