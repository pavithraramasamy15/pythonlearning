#1. Write a function in Python to read lines from a text file "notes.txt". Your function should find and display the occurrence of the word "the".
#For example: If the content of the file is:
#India is the fastest-growing economy. India is looking for more investments around the globe. The whole world is looking at India as a great market. Most of the Indians can foresee the heights that India is capable of reaching.


# f=open("notes.txt","x")
#f=open("notes.txt","w")
# f.write("India is the fastest-growing economy. India is looking for more investments around the globe. The whole world is looking at India as a great market. Most of the Indians can foresee the heights that India is capable of reaching")
# f.close()
# f=open("notes.txt","r")
# print(f.read())

def count_words():
    file = open("notes.txt","r")
    count = 0
    data = file.read()
    words = data.split()
    print(words)
    for word in words:
        if word =="the" or word =="The":  
            count += 1
    print(count)
    file.close()

count_words()
    

#2. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.
#Input:
#A boy is playing there.
#There is a playground.
#An aeroplane is in the sky.
#Alphabets & numbers are allowed in password.
#This is Path Walla Website.
#Output :-
#Word with length smaller than 3 :-
# A
# boy
# is
# is
# a
# An
# is
# in
# the
# &
# are
# in
# is
# f=open("story.txt","x")   
# f=open("story.txt","w") 
# f.write("A boy is playing there.There is a playground.An aeroplane is in the sky.Alphabets & numbers are allowed in password.This is Path Walla Website.")
# f.close()

#ANOTHER WAY

# with open("story.txt","w") as file:
#     new = file.write("A boy is playing there.There is a playground.An aeroplane is in the sky.Alphabets & numbers are allowed in password.This is Path Walla Website.")
#     file.close()

def display_words():
    file = open("story.txt","r")
    data = file.read()
    words = data.split()
    print(words)
    for word in words:
        if len(word) < 4:
            print(word)
    file.close()

# display_words()

#3.Write a Python program to add the subject_mark and update for every students in the list of dictionary format.
#Input:  [{"name":"Arun","subject_mark":{"maths":98,"Science":89,"Social":79,"Tamil":98,"English":67}}, {"name":"Bhuvan","subject_mark":{"maths":90,"Science":97,"Social":89,"Tamil":78,"English":60}}, {"name":"Rajesh","subject_mark":{"maths":70,"Science":94,"Social":99,"Tamil":85,"English":80}}]
#Output:
#[{'name': 'Arun', 'subject_mark': {'maths': 98, 'Science': 89, 'Social': 79, 'Tamil': 98, 'English': 67}, 'Total_mark': 431}, {'name': 'Bhuvan', 'subject_mark': {'maths': 90, 'Science': 97, 'Social': 89, 'Tamil': 78, 'English': 60}, 'Total_mark': 414}, {'name': 'Rajesh', 'subject_mark': {'maths': 70, 'Science': 94, 'Social': 99, 'Tamil': 85, 'English': 80}, 'Total_mark': 428}] 

def add_subject_marks(str1):
    for i in str1:
        Total_mark=sum(i["subject_mark"].values())
        i["totalmark"]=Total_mark
    return str1
   
str1=[{"name":"Arun","subject_mark":{"maths":98,"Science":89,"Social":79,"Tamil":98,"English":67}}, {"name":"Bhuvan","subject_mark":{"maths":90,"Science":97,"Social":89,"Tamil":78,"English":60}}, {"name":"Rajesh","subject_mark":{"maths":70,"Science":94,"Social":99,"Tamil":85,"English":80}}]
new_marks_list = add_subject_marks(str1)
print(new_marks_list)



#4. Write a Python function called generate_random_passwords that takes two parameters: num_passwords (an integer representing the number of passwords to generate) and length (an integer representing the length of each password). The function should generate random passwords with the following criteria: 
#Passwords starting with numbers 100 to 105 should follow a specific pattern: the number followed by a mix of uppercase letters, lowercase letters, and digits.
#For the remaining passwords, generate them randomly with a mix of uppercase letters, lowercase letters, and digits
#Expected Output:
#Password 1: 100TwGDg
#Password 2: 101F5j3v
#Password 3: 102Kp7uL
#Password 4: 103Fv2A1
#Password 5: 104dRm9z


import random
import string

def generate_random_passwords(num_passwords, length):
    passwords = []

    for i in range(1, num_passwords + 1):
        if i <= 5:
            # Passwords 1 to 5 follow a specific pattern
            password_prefix = str(100 + i)
            password_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=length - len(password_prefix)))
            new_password = f'{password_prefix}{password_suffix}'
        
        passwords.append(new_password)

    return passwords

 # Example usage with num_passwords = 5 and length = 8
result = generate_random_passwords(5, 8)

#  Print the generated passwords
for i, password in enumerate(result, start=1):
     print(f'Password {i}: {password}')


#5. Write a Python code to transform a list of lists in given input, into a dictionary of dictionaries named people_dict_of_dicts where each person is assigned a unique index, and a separate dictionary named people_indexed that categorizes individuals by their gender, listing the corresponding indices for males and females? 
#Input:  
#people_list_of_lists = [
#['John', 25, 'Male'],
#['Jane', 30, 'Female']
#['Alex', 22, 'Male'],
#['Emily', 28, 'Female'],
#['Michael', 35, 'Male'],
#['Sophia', 26, 'Female'],
#['Daniel', 31, 'Male'],
#['Olivia', 29, 'Female'],
#'William', 27, 'Male'],
#['Ava', 32, 'Female'],
#]
#Output:
#a) people_dict_of_dicts = {"1":{"name": "John", "age": 25, "gender": "Male"},"2":{"name": "Jane", "age": 30, "gender": "Female"},"3":{"name": "Alex", "age": 22, "gender": "Male"},"4":{"name": "Emily", "age": 28, "gender": "Female"},"5":{"name": "Michael", "age": 35, "gender": "Male"},"6":{"name": "Sophia", "age": 26, "gender": "Female"},"7":{"name": "Daniel", "age": 31, "gender": "Male"},"8":{"name": "Olivia", "age": 29, "gender": "Female"},"9":{"name": "William", "age": 27, "gender": "Male"},"10":{"name": "Ava", "age": 32, "gender": "Female"}}
#b) people_indexed = {"male":[1,5,7,9],"female":[2,4,6,8,10]}

people_list_of_lists = [
    ['John', 25, 'Male'],
    ['Jane', 30, 'Female'],
    ['Alex', 22, 'Male'],
    ['Emily', 28, 'Female'],
    ['Michael', 35, 'Male'],
    ['Sophia', 26, 'Female'],
    ['Daniel', 31, 'Male'],
    ['Olivia', 29, 'Female'],
    ['William', 27, 'Male'],
    ['Ava', 32, 'Female'],
]
 
emp_dict = {}
people_indexed = {'male': [], 'female': []}
 
for i, person_info in enumerate(people_list_of_lists, start=1):
    name, age, gender = person_info
    person_dict = {'name': name, 'age': age, 'gender': gender}
    emp_dict[str(i)] = person_dict
 
    if gender.lower() == 'male':
        people_indexed['male'].append(i)
    elif gender.lower() == 'female':
        people_indexed['female'].append(i)
 
print("a) people_dict_of_dicts =", emp_dict)
print("b) people_indexed =", people_indexed)
 

        
        
        
        
    


