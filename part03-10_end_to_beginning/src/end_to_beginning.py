# Write your solution here
input_string = input("Please type in a string: ")
index = len(input_string)
while index > 0:
    print(input_string[index - 1])
    index -= 1

# Solution from the site:

# input_string = input("Please type in a string: ")
# index = -1
# while index >= -len(input_string):
#     print(input_string[index])
#     index -= 1