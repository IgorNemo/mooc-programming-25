# Write your solution here
word = input("Please type in a word: ")
character = input("Please type in a character: ")
# index = word.find(character)
# length = len(word)
while len(word) >= 3:
    index = word.find(character)
    if index!=-1 and len(word)>=index+3:
        print(word[index:index+3])
        word = word[index + 1:len(word)]
    else:
        word = word[1:len(word)]

# Solution from the site:

# word = input("Please type in a word: ")
# character = input("Please type in a character: ")
 
# index = 0
 
# while index + 3 <= len(word):
#     if word[index] == character:
#         print(word[index:index+3])
#     index += 1


