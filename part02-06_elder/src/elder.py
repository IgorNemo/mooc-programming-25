# Write your solution here
name1 = input("Please type in the Name of first person: ")
age1 = int(input("Please type in the age of the first person: "))
name2 = input("Please type in the Name of second person: ")
age2 = int(input("Please type in the age of the second person: "))
if (age1 > age2):
    print(f"The elder is {name1}")
elif(age1 < age2):
    print(f"The elder is: {name2}")
else:
    print(f"{name1} and {name2} are the same age")
