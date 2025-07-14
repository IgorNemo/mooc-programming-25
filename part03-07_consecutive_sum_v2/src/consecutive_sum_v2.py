limit = int(input("Upper limit: "))
sum = "The consecutive sum: "
n = 1
s = 0
while (s < limit) and (n < limit):
    s = s + n
    if n >= (limit - 1) or s >= (limit):
        sum += f" {n}"
    else: sum += f" {n} +"
    n += 1
sum = sum + f" = {s}"
print(sum)


# Solution from site:

# limit = int(input("Limit: "))
# number = 1
# sum = 1
# numbers = "1"
# while sum < limit:
#     number += 1
#     sum += number
#     # note that f-string can also be used like this
#     numbers += f" + {number}"
# print(f"The consecutive sum: {numbers} = {sum}")
 