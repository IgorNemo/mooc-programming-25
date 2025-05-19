# Write your solution here
first_letter = input("Please type in 1st letter: ")
second_letter = input("Please type in 2nd letter: ")
third_letter = input("Please type in 3rd letter: ")
if ((first_letter < second_letter) and (first_letter > third_letter)):
    middle_letter = first_letter
elif ((second_letter < first_letter) and (second_letter > third_letter)):
        middle_letter = second_letter
elif ((third_letter < first_letter) and (third_letter > second_letter)):
        middle_letter = second_letter        
# else:
#     middle_letter = third_letter
print(f"The letter in the middle is {middle_letter}.")
