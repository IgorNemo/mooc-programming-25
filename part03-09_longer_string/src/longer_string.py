# Write your solution here
string1 = input("Please type in string 1:")
string2 = input("Please type in string 2:")
len1 = len(string1)
len2 = len(string2)
if (len1 > len2):
    lagest_string = string1 + " is longer"
else:
        if len1 < len2:
            lagest_string = string2 + " is longer"
        else:
            lagest_string = "The strings are equally long"
print(lagest_string)

