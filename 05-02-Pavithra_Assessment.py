#1. Given a complex JSON structure representing a hierarchical organization with employees and their departments, 
# write a program to extract the names of all employees who hold a managerial position in any department. 
# Ensure that the output is a sorted list of unique names. Extract the names of all employees holding a managerial position.
#INPUT:
# {					
#   "organization": {					
#     "departments": [{					
#         "name": "Engineering",					
#         "employees": [					
#           {"name": "Alice", "position": "Engineer"},					
#           {"name": "Bob", "position": "Manager"},					
#           {"name": "Charlie", "position": "Engineer"}					
#         ]					
#       },					
#       {					
#         "name": "Sales",					
#         "employees": [					
#           {"name": "David", "position": "Salesperson"},					
#           {"name": "Eve", "position": "Manager"}					
#         ]					
#       }					
#     ]					
#   }					
# }		
#output:
#['Bob', 'Eve']
	


def manager(data):
    manageremp = set()

    for department in data.get("organization", {}).get("departments", []):
        for employee in department.get("employees", []):
            if employee.get("position", "").lower() == "manager":
                manageremp.add(employee.get("name", ""))

    sortemp = sorted(list(manageremp))
    return sortemp
import json

input_json = '{"organization": {"departments": [{"name": "Engineering","employees": [{"name": "Alice", "position": "Engineer"},{"name": "Bob", "position": "Manager"},{"name": "Charlie", "position": "Engineer"}]},{"name": "Sales","employees": [{"name": "David", "position": "Salesperson"},{"name": "Eve", "position": "Manager"}]}] }}'

data = json.loads(input_json)
print(input_json)
print(data)
print(type(input_json))
print(type(data))


result = manager(data)
print(result)

    
#2. Given a nested JSON structure representing a file system, write a program to find the total size occupied by files in a specific directory and its subdirectories.
#input:
json_data = {						
  "name": "root",						
  "type": "directory",						
  "size": None,						
  "contents": [						
    {						
      "name": "folder1",						
      "type": "directory",						
      "size": None,						
      "contents": [						
        {"name": "file1.txt", "type": "file", "size": 1024},						
        {"name": "file2.txt", "type": "file", "size": 512}						
      ]						
    },						
    {						
      "name": "folder2",						
      "type": "directory",						
      "size": None,						
      "contents": [						
        {"name": "file3.txt", "type": "file", "size": 256},						
        {"name": "file4.txt", "type": "file", "size": 128}						
      ]						
    },						
    {"name": "file5.txt", "type": "file", "size": 64}						
  ]						
}	


def calculate_total_size(contents):
    total_size = 0
    directories = [contents]
   
    for directory in directories:
        for item in directory:
            if item["type"] == "file":
                total_size += item["size"]
            elif item["type"] == "directory":
                for sub_item in item["contents"]:
                    if sub_item["type"] == "file":
                        total_size += sub_item["size"]
                    elif sub_item["type"] == "directory":
                        sub_item.append(sub_item["contents"])
   
    return total_size
 
print(calculate_total_size(json_data["contents"]))


#3. Write a program to transform a JSON structure representing a list of students and their grades into a report card, including the average grade for each student and the class average. ALos sort the order of average from highest to lowest inside report card
# Input:												
# {												
#   "students": [												
#     {"name": "Alice", "grades": [90, 85, 92]},												
#     {"name": "Bob", "grades": [78, 88, 94]},												
#     {"name": "Charlie", "grades": [92, 95, 89]}												
#   ]												
# }												
												
# Output:												
# Report Card:												
# [{'name': 'Charlie', 'average_grade': 92.0}, {'name': 'Alice', 'average_grade': 89.0}, {'name': 'Bob', 'average_grade': 87.0}]												
# Class Average: 89		

import json
import math
 
def generate_reportcard(input_json):
    def sort_by_average_grade(student):
        return student["average_grade"]
 
    students = input_json["students"]
    report_card = []
 
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average_grade = sum(grades) / len(grades)
        report_card.append({"name": name, "average_grade": average_grade})
 
   
    report_card.sort(key=sort_by_average_grade, reverse=True)
 
   
    class_total = sum(student["average_grade"] for student in report_card)
    class_average = math.floor(class_total / len(report_card))
   
    return report_card, class_average
 
input_json = {"students": [
    {"name": "Alice", "grades": [90, 85, 92]},
    {"name": "Bob", "grades": [78, 88, 94]},
    {"name": "Charlie", "grades": [92, 95, 89]}
]}
 
report_card, class_average = generate_reportcard(input_json)
 
 
print("Report Card:")
print(report_card)
 
 
print("Class Average:", class_average)


#4. You are given two lists: one containing names and the other containing corresponding birth years. 
# Your task is to manipulate these lists and generate key-value pairs with the name as the key and age as the value. 
# Calculate the age based on the given birth year and today's date. Then, create a JSON structure to represent this information. 
# Additionally, calculate the average age of the individuals and include it in the JSON output. 

#Input:					
# names = ["Alice", "Bob", "Charlie", "David", "Eve"]					
# birth_years = [1980, 1978, 1991, 1971, 1995]	

# Output should be in json format:				
# {				
#   "above_40": {				
#     "Alice": 44,				
#     "Bob": 46,				
#     "David": 53				
#   },				
#   "below_40": {				
#     "Charlie": 33,				
#     "Eve": 29				
#   },				
#   "statistics": {				
#     "count_above_40": 3,				
#     "count_below_40": 2				
#   }				
# }

from datetime import date
import json

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
birth_years = [1980, 1978, 1991, 1971, 1995]

today_date = date.today()

age_list = [today_date.year - birth_year for birth_year in birth_years]

above_40 = {}
below_40 = {}

for name, age in zip(names, age_list):
    if age >= 40:
        above_40[name] = age
    else:
        below_40[name] = age

above_40_count = len(above_40)
below_40_count = len(below_40)

statistics = {
    "above_40": above_40,
    "below_40": below_40,
    "statistics": {
        "count_above_40": above_40_count,
        "count_below_40": below_40_count
    }
}

print(statistics)
statistics_json = json.dumps(statistics, indent=2)

print(type(statistics_json))



#5. You are provided with a JSON structure representing a list of employees in a company. Each employee has information such as name, department, and salary. Write a program to identify the highest-paid employee in each department and generate a new JSON structure with the department names and the corresponding highest-paid employee details.						
						
# Input:						
# {						
#   "employees": [						
#     {"name": "Alice", "department": "HR", "salary": 60000},						
#     {"name": "Bob", "department": "Engineering", "salary": 80000},						
#     {"name": "Charlie", "department": "HR", "salary": 70000},						
#     {"name": "David", "department": "Sales", "salary": 75000},						
#     {"name": "Eve", "department": "Engineering", "salary": 90000}						
#   ]						
# }						
# Output:						
# {						
#   "highest_paid_employees": [						
#     {"department": "HR", "highest_paid_employee": {"name": "Charlie", "salary": 70000}},						
#     {"department": "Engineering", "highest_paid_employee": {"name": "Eve", "salary": 90000}},						
#     {"department": "Sales", "highest_paid_employee": {"name": "David", "salary": 75000}}						
#   ]						
# }		


import json
 
def highest_paid_employees(employees):
   
    department_highest_paid = {}
 
    for employee in employees:
       
        department = employee["department"]
        salary = employee["salary"]
 
        if department in department_highest_paid:
            if salary > department_highest_paid[department]["salary"]:
                department_highest_paid[department] = {"name": employee["name"], "salary": salary}
        else:
            department_highest_paid[department] = {"name": employee["name"], "salary": salary}
 
    highest_paid_employees_list = [{"department": dept, "highest_paid_employee": details} for dept, details in department_highest_paid.items()]
    return {"highest_paid_employees": highest_paid_employees_list}
 
input_json = {"employees": [{"name": "Alice", "department": "HR", "salary": 60000},{"name": "Bob", "department": "Engineering", "salary": 80000},{"name": "Charlie", "department": "HR", "salary": 70000},{"name": "David", "department": "Sales", "salary": 75000},{"name": "Eve", "department": "Engineering", "salary": 90000}]}
 
output_json = highest_paid_employees(input_json["employees"])
 
print("Output: ", json.dumps(output_json, indent=2))
print("Output type: ", type(output_json))				