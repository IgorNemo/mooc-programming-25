# Write your solution here
quantity_lunch_per_week = int(input("How many times a week do you eat at the student cafeteria? "))
price_lunch = float(input("The price of a typical student lunch? "))
money_grocery_per_week = float(input("How much money do you spend on groceries in a week? "))
expenditure_lunch_per_week = quantity_lunch_per_week * price_lunch
print("Average food expenditure:")
print(f"Daily: {(expenditure_lunch_per_week + money_grocery_per_week)/7} euros")
print(f"Weekly: {(expenditure_lunch_per_week + money_grocery_per_week)} euros")
