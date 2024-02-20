'''
1. Run this below code in your terminal,
import json
import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_json(depth):
    if depth <= 0:
        return random.choice([None, random.randint(0, 100), generate_random_string(random.randint(5, 10))])

    result = {}
    for _ in range(random.randint(10, 20)):
        key = generate_random_string(random.randint(3, 7))
        result[key] = generate_random_json(depth - 1)

    return result

random_json = generate_random_json(3)

with open("random_data.json", "w") as json_file:
    json.dump(random_json, json_file, indent=4)   

print("Random JSON data stored in 'random_data.json'")


you can see an random json data created in the directory, now use that given random data, find out the total number of keys, values, null values,

Expected output should be like below with each :
Total number of keys: 
Total number of values:
Total number of null values:
'''

import json
with open ("random_data.json","r") as file:
    random_data=json.load(file)
    print(type(random_data))
def count_json(random_data):
    total_keys = 0 
    total_values = 0
    total_null_values = 0
    for key, value in random_data.items():
        total_keys += 1
        if isinstance(value,dict):
            sub_keys, sub_values, sub_null_values = count_json(value)
            total_keys += sub_keys 
            total_values += sub_values
            total_null_values += sub_null_values
        elif value is None:
            total_null_values += 1
        else:
            total_values += 1
    return total_keys, total_values, total_null_values
total_keys, total_values, total_null_values = count_json(random_data)
print("Total number of keys:", total_keys)
print("Total number of values:", total_values)
print("Total number of null values:",total_null_values)


'''
2.Write a program to build a simple Student Management System using Python which can perform the following operations:

Accept
Display
Search
Delete
Update

Expected Output:
Operations used,
a.Accept Student details
b.Display Student Details
c.Search Details of a Student
d.Delete Details of Student
e.Update Student Details
f.Exit

List of Students
Name   :  A
RollNo :  1
Marks1 :  100
Marks2 :  100

Name   :  B
RollNo :  2
Marks1 :  90
Marks2 :  90

Name   :  C
RollNo :  3
Marks1 :  80
Marks2 :  80

Student Found,
Name   :  B
RollNo :  2
Marks1 :  90
Marks2 :  90

List after deletion
Name   :  A
RollNo :  1
Marks1 :  100
Marks2 :  100

Name   :  C
RollNo :  3
Marks1 :  80
Marks2 :  80

List after updation
Name   :  A
RollNo :  1
Marks1 :  100
Marks2 :  100

Name   :  C
RollNo :  2
Marks1 :  80
Marks2 :  80
'''
class student():
    def __init__(self,name,rollno,marks1,marks2):
        self.name=name
        self.rollno=rollno
        self.marks1=marks1
        self.marks2=marks2
    def display(self):
        print("Name:",self.name)
        print("RollNo:",self.rollno)
        print("Marks1:",self.marks1)
        print("Marks2:",self.marks2)
def accept():
    name=input("Enter the Name:")
    rollno=int(input("Enter the rollno:"))
    marks1=int(input("Enter the marks1:"))
    marks2=int(input("Enter the marks2:"))
    return student(name,rollno,marks1,marks2) 
    

def display_students(emplist):
    print("list of students")
    for i in emplist:
        i.display()
        
def search(emplist,rollno):
     for i in emplist:
        if i.rollno==rollno:
            print("Student Found")
            i.display()
        else:
            print("student not found")
        
def delete(emplist,rollno):
    for i in emplist:
        if i.rollno==rollno:
            emplist.remove(i)
    print("List after deletion")
    i.display()
def update(emplist,rollno):
    for i in emplist:
        if i.rollno==rollno:
            print("Enter Updated details")
            updated=accept()
            emplist.append(updated)
    print("List after updated")
    i.display()
def system():
    emplist=[]
    while True:
        print("Operations Used")
        print("a.Accept Student Details:")
        print("b.Display Student Details:")
        print("c.Search Details of a Student: ")
        print("d.Delete Details of a Student:")
        print("e.Update Student Details:")
        print("f.Exit")
        letter=input("Enter the letter(a-f):")
        if letter=='a':
            emplist.append(accept())
        elif letter=='b':
            display_students(emplist)
        elif letter=='c':
            rollno=int(input("Enter the rollno to search:"))
            search(emplist,rollno)
        elif letter=='d':
            rollno=int(input("Enter the rollno to delete:"))
            delete(emplist,rollno)
        elif letter=='e':
            rollno=int(input("Enter the rollno to update student details:"))
            update(emplist,rollno)
        elif letter=='f':
            print("Exit")
            break
        else:
            print("Enter the valid letter")   
            
output1=system()
print(output1)            
            