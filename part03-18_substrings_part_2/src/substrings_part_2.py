# Write your solution here
word = input("Please type in a string: ")
n = len(word)
while n > 0:
    print(word[n - 1:len(word)])
    n -= 1

# Solution from the site:

# string = input("Please type in a string: ")
 
# start = len(string) - 1
# while start >= 0:
#     print(string[start:])
#     start -= 1