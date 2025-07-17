# Write your solution here
word = input("Word: ")
p = len(word)
m = (30 - p)
n = m // 2
print("*" * 30)
if m % 2 == 0:
    print("*" + " " * (n - 1) + word + " " * (n - 1) + "*")
else:
    print("*" + " " * n + word + " " * (n - 1) + "*")
print("*" * 30)


# Solution from the site:

# word = input("Word: ")
 
# print("*" * 30)
# spaces_at_start = (28 - len(word)) // 2
# spaces_at_end = spaces_at_start
 
# # If the word length is odd, one is added to the spaces at the end of the word
# # to get all 30 characters filled
# if len(word) % 2 != 0:
#     spaces_at_end += 1
 
# print("*" + spaces_at_start * " " + word + spaces_at_end * " " + "*")
# print("*" * 30)
