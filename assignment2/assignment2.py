import csv
import os
import custom_module
#Task 2: Read a CSV File


def read_employees():
    employees_dict = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)

            for i, row in enumerate(reader):
                if i == 0:
                    employees_dict["fields"] = row
                else:
                    rows.append(row)

        employees_dict["rows"] = rows
        return employees_dict

    except Exception as e:
        print("An exception occurred.")
        print(type(e).__name__)
        exit()

# for test
employees = read_employees()
#print(employees)

# Task 3 Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)


employee_id_column = column_index("employee_id")

#Task 4 : Find the Employee First Name
def first_name(row_number):
    index = column_index("first_name")
    return employees["rows"][row_number][index]

#Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches

#Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches


#Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    idx = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[idx])
    return employees["rows"]


sort_by_last_name()
#print(employees)
#print([row[2] for row in employees["rows"]])


#Task 8: Create a dict for an Employee
def employee_dict(row):
    result = {}

    for i, field in enumerate(employees["fields"]):
        if field == "employee_id":
            continue
        result[field] = row[i]

    return result
#Task 8: Create a dict for an Employee


def employee_dict(row):
    result ={}
    
    for i, field in enumerate(employees["fields"]):
        if field == "employee_id":
            continue
        result[field] = row[i]
    return result
#print(employee_dict(employees["rows"][0]))

#Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    result ={}
    
    for row in employees["rows"]:
        emp_id = row[employee_id_column]
        result[emp_id] = employee_dict(row)

    return result

#print(all_employees_dict())

#Task 10: Use the os Module


def get_this_value():
    return os.getenv("THISVALUE")


#Task 11: Creating Your Own Module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
    
    
#print(custom_module.secret)

#Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():

    def read_file(file_name):
        data = {"fields": [], "rows": []}

        with open(file_name, "r") as file:
            reader = csv.reader(file)

            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    data["rows"].append(tuple(row))

        return data

    minutes1 = read_file("../csv/minutes1.csv")
    minutes2 = read_file("../csv/minutes2.csv")

    return minutes1, minutes2


minutes1, minutes2 = read_minutes()
# print(minutes1)
# print(minutes2)

#Task 13: Create minutes_set
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1 | set2

minutes_set = create_minutes_set()  

#Task 14: Convert to datetime
from datetime import datetime

def create_minutes_list():
    minutes_set = create_minutes_set() 
    
    minutes_list = list(minutes_set)

    return list(map(
        lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
        minutes_list
    ))

minutes_list = create_minutes_list()

#print(minutes_list)

#Task 15: Write Out Sorted List

def write_sorted_list():

    # sort by datetime object
    sorted_list = sorted(minutes_list, key=lambda x: x[1])

    # convert datetime to string
    converted = list(map(
        lambda x: (x[0], x[1].strftime("%B %d, %Y")),
        sorted_list
    ))

    # write to CSV
    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)

      
        writer.writerow(minutes1["fields"])

     
        writer.writerows(converted)

    return converted
    