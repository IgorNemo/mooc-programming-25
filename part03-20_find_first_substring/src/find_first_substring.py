# Write your solution here
word = input("Please type in a word: ")
character = input("Please type in a character: ")
index = word.find(character)
length = len(word)
if length >= index + 3:
    print(word[index:index + 3])

# Solution from the site:

# word = input("Please type in a word: ")
# character = input("Please type in a character: ")
 
# index = word.find(character)
# if index!=-1 and len(word)>=index+3:
#     print(word[index:index+3])

