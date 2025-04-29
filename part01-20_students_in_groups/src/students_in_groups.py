# Write your solution here
quantity_students = int(input("How many students on the course? "))
desired_group_size = int(input("Desired group size? "))
a = quantity_students // desired_group_size
b = quantity_students % desired_group_size
c = b > 0
d = int(c)
number_groups = a + d
print(f"Number of groups formed: {number_groups}")
