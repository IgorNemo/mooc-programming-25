# Write your solution here
year = int(input("Please type in a year: "))
if ((year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))):
    print("That year is a leap year.")
else: print("That year is not a leap year.")  

# Solution from the TMC:
year = int(input("Please type in a year: "))
 
# First, we make assumption that a year is not a leap year
leap_year = False
 
if year % 100 == 0:
    if year % 400 == 0:
        leap_year = True
elif year % 4 == 0:
    leap_year = True
 
if leap_year:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")
  
# if (year % 4 == 0 and year % 100 == 0):
#     if (year % 400 == 0):
        #  print("That year is a leap year.")
# if (year % 4 == 0 and not (year % 100 == 0)):
#     print("That year is a leap year.")
# if (not (year % 4 == 0)):
#     print("That year is not a leap year.")
# if (year == 500):
#     print("That year is not a leap year.")
# if (year == 700):
#     print("That year is not a leap year.")
# if (year == 1100):
#     print("That year is not a leap year.")    