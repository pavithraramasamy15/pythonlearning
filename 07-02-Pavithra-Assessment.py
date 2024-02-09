#1. Given a JSON structure representing employees and their skills, write a Python program to generate a new JSON structure mapping each skill to the employees possessing that skill.
# Input
# { 
# "employees": [
#     {"name": "Alice", "skills": ["Python", "Java"]},
#     {"name": "Bob", "skills": ["C++", "Python", "JavaScript"]},
#     {"name": "Charlie", "skills": ["Java", "JavaScript"]},
#     {"name": "David", "skills": ["Python", "C#"]},
#     {"name": "Eve", "skills": ["JavaScript", "HTML", "CSS"]}
#   ]
# }


# Output:
# {
#   "skill_mapping": {
#     "Python": ["Alice", "Bob", "David"],
#     "Java": ["Alice", "Charlie"],
#     "C++": ["Bob"],
#     "JavaScript": ["Bob", "Charlie", "Eve"],
#     "C#": ["David"],
#     "HTML": ["Eve"],
#     "CSS": ["Eve"]
#   }
# }

import json


input_json ={
  "employees": [
    {"name": "Alice", "skills": ["Python", "Java"]},
    {"name": "Bob", "skills": ["C++", "Python", "JavaScript"]},
    {"name": "Charlie", "skills": ["Java", "JavaScript"]},
    {"name": "David", "skills": ["Python", "C#"]},
    {"name": "Eve", "skills": ["JavaScript", "HTML", "CSS"]}
  ]
}





empskill= {}


for employee in input_json["employees"]:
    
    for skill in employee["skills"]:
      
        if skill in empskill:
            empskill[skill].append(employee["name"])
      
        else:
            empskill[skill] = [employee["name"]]

output_json = {"skillmapping": empskill}
print(json.dumps(output_json, indent=2))



# 2)consider below json structure data, 
json_data={
  "company": "InnovateTech",
  "location": "Metropolis",
  "departments": [
    {
      "name": "Engineering",
      "manager": "Amit Sharma",
      "employees": [
        {
          "id": 1,
          "name": "Sunita Patel",
          "position": "Software Engineer",
          "salary": 95000,
          "projects": [
            {
              "name": "AI Chatbot Development",
              "status": "In Progress"
            },
            {
              "name": "Data Analytics Dashboard",
              "status": "Completed"
            }
          ]
        },
        {
          "id": 2,
          "name": "Rahul Singh",
          "position": "DevOps Engineer",
          "salary": 105000,
          "projects": [
            {
              "name": "Continuous Integration Pipeline",
              "status": "In Progress"
            }
          ]
        },
        {
          "id": 3,
          "name": "Deepa Sharma",
          "position": "Frontend Developer",
          "salary": 90000,
          "projects": [
            {
              "name": "User Interface Redesign",
              "status": "Completed"
            }
          ]
        }
      ]
    },
    {
      "name": "Marketing",
      "manager": "Neha Verma",
      "employees": [
        {
          "id": 4,
          "name": "Aryan Khan",
          "position": "Marketing Manager",
          "salary": 110000,
          "campaigns": [
            {
              "name": "Product Launch Campaign",
              "status": "In Progress"
            }
          ]
        },
        {
          "id": 5,
          "name": "Neha Gupta",
          "position": "Digital Marketer",
          "salary": 80000,
          "campaigns": [
            {
              "name": "Social Media Campaign",
              "status": "Completed"
            }
          ]
        }
      ]
    }
  ]
}







# a) Given the JSON data provided, write a function that returns the total number of completed projects across all departments.
# Expected output: Total number of completed projects: 2


import json

def completepro(json_data):
    total = 0
    for i in json_data["departments"]:
        for j in i["employees"]:
            for project in j.get("projects", []):
                if project["status"] == "Completed":
                    total += 1
    return total

print(completepro(json_data))


# b) Using the JSON data, generate a report that lists all employees along with their positions and salaries, sorted in descending order of salaries.
# Expected Output: 
# Employee Report:
# Name: Aryan Khan, Position: Marketing Manager, Salary: 110000
# Name: Rahul Singh, Position: DevOps Engineer, Salary: 105000
# Name: Sunita Patel, Position: Software Engineer, Salary: 95000
# Name: Deepa Sharma, Position: Frontend Developer, Salary: 90000
# Name: Neha Gupta, Position: Digital Marketer, Salary: 80000



def sort_by_salary(employee):
    return employee[2]



def generate_employee_report(json_data):
    report = []
    for department in json_data["departments"]:
 
        for employee in department["employees"]:
            report.append(
                {
                    "Name": employee["name"],
                    "Position": employee["position"],
                    "Salary": employee["salary"],
                }
            )
    report_sorted = sorted(report, key=lambda x:x["Salary"], reverse=True)
    return report_sorted


employee_report=generate_employee_report(json_data)
print(employee_report)

for employee in employee_report:
    print(f"Name: {employee['Name']}, Position: {employee['Position']}, Salary: {employee['Salary']}")
    
 
 
# c) Extend the JSON data to include a new department called "Finance" with a manager named "Rajesh Kumar". Then, write a function to update the JSON with a new employee in the Finance department. The new employee's details are:

# Name: Priya Mehta
# Position: Financial Analyst
# Salary: 95000
# Expected output: given details should be added to existing json and print the updated json in terminal.

import json
newemp = {"name": "Priya Mehta","position": "Financial Analyst","salary": 95000 }
json_data["departments"].append({"name": "Finance","manager": "Rajesh Kumar","employees": [newemp]})
print(json.dumps(json_data, indent=2))

# d) Utilizing the provided JSON, create a report that lists all ongoing projects, along with the department they belong to and their respective managers.

# Expected Output:
# Ongoing Projects Report:
# Project: AI Chatbot Development, Department: Engineering, Manager: Amit Sharma
# Project: Continuous Integration Pipeline, Department: Engineering, Manager: Amit Sharma
# Project: Product Launch Campaign, Department: Marketing, Manager: Neha Verma


def generate_ongoing_projects_report(json_data):
    report = []
    for department in json_data["departments"]:
        for employee in department["employees"]:
            for project in employee.get("projects") or employee.get("campaigns"):
                if project["status"] == "In Progress":
                    report.append(
                        {
                            "Project": project["name"],
                            "Department": department["name"],
                            "Manager": department["manager"],
                           
                        }
                    )
    return report
 
result = generate_ongoing_projects_report(json_data)
 
for res in result:
    print(f'Project:{res["Project"]}, Department:{res["Department"]}, Manager:{res["Manager"]}')
    
# e) Given the JSON structure, write a function that calculates the average salary for each department.
# Expected Output:
# Average Salaries for Each Department:
# Engineering: 96833.33333333333
# Marketing: 95000.0
# Finance: 95000.0


def averagesal(json_data):
    department_salaries = {}
    for department in json_data["departments"]:
        department_name = department["name"]
        total_salary = 0
        num_employees = 0
        for employee in department["employees"]:
            total_salary += employee["salary"]
            num_employees += 1
        if num_employees > 0:
            average_salary = total_salary / num_employees
            department_salaries[department_name] = average_salary

    return department_salaries
average_salaries = averagesal(json_data)
print("Average Salaries for Each Department:")
for department, average_salary in average_salaries.items():
    print(f"{department}: {average_salary}")
    


