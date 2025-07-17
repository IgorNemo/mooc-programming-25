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
