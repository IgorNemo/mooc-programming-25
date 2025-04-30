# Write your solution here
hourly_wage = float(input("Please type in hourly wage: "))
hours_worked = float(input("Please type in hours worked: "))
day_of_week = input("Please type in Day of the week: ")
daily_wages = hourly_wage * hours_worked
if day_of_week == "Sunday":
    daily_wages *= 2
print(f"Daily wages: {daily_wages} euros")


