from math import sqrt
# Write your solution here
while True:
    number = int(input("Please type in a number: "))
    if number == 0:
        print("Exiting...")
        break
    elif number < 0:
        print("Invalid number")
    elif number > 0:
        numbersqrt = sqrt(number)
        print(numbersqrt)
