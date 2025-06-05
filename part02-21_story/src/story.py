# Write your solution here
word1 = ""
string = ""
while True:
    word2 = word1
    string += " " + word1
    word1 = input("Please type in a word: ")
    if ((word1 == "end") or (word2 == word1)):
        print(string)
        break
