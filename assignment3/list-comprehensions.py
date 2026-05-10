#Task 3: List Comprehensions Practice
import csv

employees = []
with open('../csv/employees.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        employees.append(row)
        
names = [
    row[0] + " " + row[1]
    for row in employees[1:]
]

names_with_e = [name for name in names if "e" in name]


print(names)
print(names_with_e)

#append new first and lastname to list
# new_first_name = input("Enter a new first name: ")
# new_last_name = input("Enter a new last name: ")
# names.append(new_first_name + " " + new_last_name)
# print(names)


