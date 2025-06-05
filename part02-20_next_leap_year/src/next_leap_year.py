# Write your solution here
year = int(input("Please type in a year: "))
n = year + 1
while True:
    if ((n % 4 == 0) and ((n % 100 != 0) or (n % 400 == 0))):
        leapyear = n
        break
    n += 1
print(f"The next leap year after {year} is {leapyear}")
