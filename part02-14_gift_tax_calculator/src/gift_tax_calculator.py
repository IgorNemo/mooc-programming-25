# Write your solution here
gift = int(input("Please type in value of gift: "))
if gift < 5000:
    tax = 0
    taxch = "No tax!"
elif gift >= 1000000:
    tax = 142100 + (gift - 1000000) * 0.17
    taxch = str(tax) + " euros"
elif gift >= 200000:
    tax = 22100 + (gift - 200000) * 0.15
    taxch = str(tax) + " euros"
elif gift >= 55000:
    tax = 4700 + (gift - 55000) * 0.12
    taxch = str(tax) + " euros"
elif gift >= 25000:
    tax = 1700 + (gift - 25000) * 0.10
    taxch = str(tax) + " euros"
else:
    tax = 100 + (gift - 5000) * 0.08
    taxch = str(tax) + " euros"
print(f"Amount of tax: {taxch}")
