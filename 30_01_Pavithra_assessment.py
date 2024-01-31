# 1. Write a Python program to filter a dictionary based on values.
#Input:
#Original Dictionary:
#{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
#Output:
#Marks greater than 170:
#{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}

original_dict={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}

def filter_condition(original_dict):
    emp_dict = {}
    
    for key,value in original_dict.items():
        if value>170:
            emp_dict[key]=value
    return emp_dict
result=filter_condition(original_dict)
print(result)
#2. Write a Python program to convert more than one list to a nested dictionary.
#Input : 
#Original strings:
#['S001', 'S002', 'S003', 'S004']
#['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
#[85, 98, 89, 92]
#Output:
#Nested dictionary:
#[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]       
 
original_string1=['S001','S002','S003','S004']
original_string2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
original_string3=[85, 98, 89, 92]
nested_dict={}
for i in range(len(original_string1)):
    dict1={original_string2[i]:original_string3[i]}
    nested_dict[original_string1[i]]=dict1
print("Nested Dictionary:" +str(nested_dict))

# Another way
def nested_dict(s1,s2,s3):
    newdict=[{x:{y,z}} for (x,y,z) in zip(s1,s2,s3)]
    return newdict
print(nested_dict(original_string1,original_string2,original_string3))

#3. Write a Python program to extract and print the phone number of a specific employee from a nested dictionary.
#Input:
#employee_data = {
#    'Alice': {'position': 'Manager', 'phone': '123-456-7890'},
#    'Bob': {'position': 'Developer', 'phone': '987-654-3210'},
#  'Charlie': {'position': 'Analyst', 'phone': '555-123-4567'}
#  }          

employee_data = {
   'Alice': {'position': 'Manager', 'phone': '123-456-7890'},
   'Bob': {'position': 'Developer', 'phone': '987-654-3210'},
 'Charlie': {'position': 'Analyst', 'phone': '555-123-4567'}
 } 
def getnumber(employee_data, employee_name):
    if employee_name in employee_data:
        return employee_data[employee_name]['phone']
    else:
        return None
target_employee = 'Bob'
phone_number = getnumber(employee_data, target_employee)
print(f"The phone number of {target_employee} is: {phone_number}")

    


#4. You are given a nested dictionary representing a catalog of products in an online store. Each product has various attributes such as name, price, and availability. Write a Python program to find and print the names of products that are both affordable (price less than $50) and currently available.
#Input:
#product_catalog = {
#'Laptop': {'price': 1200, 'availability': True},
#'Headphones': {'price': 30, 'availability': True}, 
#'Smartphone': {'price': 600, 'availability': False},   
#'Tablet': {'price': 40, 'availability': True},     
#'Camera': {'price': 150, 'availability': False}
#   }
#Expected Output:
#Affordable and Available Products:
#['Headphones', 'Tablet']

product_catalog = {
'Laptop': {'price': 1200, 'availability': True},
'Headphones': {'price': 30, 'availability': True}, 
'Smartphone': {'price': 600, 'availability': False},   
'Tablet': {'price': 40, 'availability': True},     
'Camera': {'price': 150, 'availability': False}
   }

def affordableandavailable(product_catalog):
    affordableandavailable = []

    for i, j in product_catalog.items():
        price = j['price']
        availability = j['availability']

        if price < 50 and availability:
            affordableandavailable.append(i)

    return affordableandavailable
result = affordableandavailable(product_catalog)
print("Affordable and Available Products:")
print(result)






    


  
