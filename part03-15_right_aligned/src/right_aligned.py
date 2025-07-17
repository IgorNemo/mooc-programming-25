# Write your solution here
string = input("Please type in a string: ")
if len(string) == 20:
        print(string)
else:
    print("*" * (20 - len(string)) + string)


# Solution from the site:

# word = input("Please type in a string: ") 
# aligned = (20 - len(word)) * "*" + word 
# print(aligned)
