# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
count = 0
sum = 0
negative = 0
positive =0
while True:
    number = int(input())
    if (number == 0):
        break
    count += 1
    sum += number
    if number < 0:
       negative += +1
    elif number > 0:
        positive += +1
print("Numbers typed in " + str(count))
print(f"The sum of the numbers is {sum}")
if count > 0:
    mean = sum / count
    print(f"The mean of the numbers is {mean}")
else:
    print("The mean of the numbers is: N/A")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")