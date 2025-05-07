# Write your solution here
number = int(input("Number: "))
if (number / 3 - number // 3 == 0):
    if (number / 5 - number // 5 == 0):
        print("FizzBuzz")
    else: print("Fizz")
elif (number / 5 - number // 5 == 0):
    print("Buzz")
