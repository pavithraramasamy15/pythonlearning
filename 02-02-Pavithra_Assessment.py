#1. Write a function to eliminate all special characters for each of strings in a list and just return back alpha strings for each in a list
#Input:
#['nB~!@#$%^23', 'Gh&*45vD9zL', 'qW@3yU%1r+7X', 'p$*8JmVcBn6F', 'k!2oT&7sPmQ"(l']
#Output:
#['nB23', 'Gh45vD9zL', 'qW3yU1r7X', 'p8JmVcBn6F', 'k2oT7sPmQl']
import re

def elimisplchr(input_list):
    result=[]
    for s in input_list:
        alphastr=re.sub('[^a-zA-Z0-9]',"",s)
        result.append(alphastr)
    return result



input_list = ['nB~!@#$%^23', 'Gh&*45vD9zL', 'qW@3yU%1r+7X', 'p$*8JmVcBn6F', 'k!2oT&7sPmQ"(l']
output_list =  elimisplchr(input_list)
print(output_list)

#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

#2. Write a function to manipulate the values of list of dictionary. for example, if its int, multiply with 2, str means reverse it, float means, round to nearby number,
#Input:
#list_of_dicts = [
#{'a': 5, 'b': 'hello', 'c': 3.14},
#{'x': 10, 'y': 'world', 'z': 7.5}
#]
#Output:
#[{'a': 10, 'b': 'olleh', 'c': 3}, {'x': 20, 'y': 'dlrow', 'z': 8}]

def manipulate_list_of_dicts(list_of_dicts):
    manipulated_list = []

    for dictionary in list_of_dicts:
        manipulated_dict = {}
        for key, value in dictionary.items():
            if isinstance(value, int):
                manipulated_dict[key] = value * 2
            elif isinstance(value, str):
                manipulated_dict[key] = value[::-1]
            elif isinstance(value, float):
                manipulated_dict[key] = round(value)
            else:
                manipulated_dict[key] = value

        manipulated_list.append(manipulated_dict)

    return manipulated_list
list_of_dicts = [
    {'a': 5, 'b': 'hello', 'c': 3.14},
    {'x': 10, 'y': 'world', 'z': 7.5}
]
result = manipulate_list_of_dicts(list_of_dicts)
print(result)

#The isinstance() function returns True if the specified object is of the specified type, otherwise False.


#3. Write a function to manipulate the values of below input as expected
#Input:
#input_dict = {
#    'word1': 'hello',
#    'word2': 'level',
#    'word3': 'example',
#    'word4': 'racecar'
#}
#Output: {'word1': 'oll*h', 'word2': 'l*v*l - palindrome', 'word3': '*lpmax*', 'word4': 'rac*car - palindrome'}



def process_words(input_dict):
    output_dict = {}
    
    for key, value in input_dict.items():
        reversed_value = value[::-1]
        replace_value=reversed_value.replace('e','*')
        if reversed_value==value:
            output_dict[key]= f'{replace_value} - palindrome'
        else:
            output_dict[key] =replace_value

    return output_dict

input_dict = {
    'word1': 'hello',
    'word2': 'level',
    'word3': 'example',
    'word4': 'racecar'
}

output_dict = process_words(input_dict)
print(output_dict)


#4. Given a dictionary with string keys and integer values, transform it into a new dictionary where the keys are the lengths of the original keys, and the values are lists of keys of that length. 
#Input:
#original_dict = {'apple': 5, 'banana': 6, 'orange': 6, 'kiwi': 4, 'grape': 5}
#Output:
#transformed_dict = {4: ['kiwi'], 5: ['apple', 'grape'], 6: ['banana', 'orange']}

def transform_dictionary(original_dict):
    transformed_dict = {}

    for key, value in original_dict.items():
        key_length = len(key)
        if key_length not in transformed_dict:
            transformed_dict[key_length] = [key]
        else:
            transformed_dict[key_length].append(key)

    return transformed_dict


original_dict = {'apple': 5, 'banana': 6, 'orange': 6, 'kiwi': 4, 'grape': 5}

transformed_dict = transform_dictionary(original_dict)

print(transformed_dict)




#5. Given a list of dictionaries representing student information, where each dictionary has keys 'name', 'subject', and 'marks', write a Python function to transform the list into a dictionary where each subject is a key, and the value is a list of students who scored the highest marks in that subject.
#Input:
#student_data = [
#    {'name': 'Alice', 'subject': 'Math', 'marks': 90},
#    {'name': 'Bob', 'subject': 'Math', 'marks': 85}
#    {'name': 'Alice', 'subject': 'Physics', 'marks': 88},
#    {'name': 'Bob', 'subject': 'Physics', 'marks': 92},
#    {'name': 'Alice', 'subject': 'Chemistry', 'marks': 78},
#    {'name': 'Bob', 'subject': 'Chemistry', 'marks': 88}
#]
#Output:
#highest_scorers = {
#    'Math': ['Alice'],
#    'Physics': ['Bob'],
#    'Chemistry': ['Bob']
#}

def highscore(student_data):
    highest_scorers={}
    for e in student_data:
        subject=e['subject']
        name=e['name']
        marks=e['marks']
        if subject in highest_scorers:
            if marks>highest_scorers[subject]['marks']:highest_scorers[subject]={'marks':marks,'student':[name]}
            elif marks==highest_scorers[subject]['marks']:highest_scorers[subject]['students'].append(name)
            else:
                highest_scorers[subject]={'marks':marks,'students':[name]}
                result={subject:data['students'] for subject,data in highest_scorers.items()}
                return result
    




student_data = [
     {'name': 'Alice', 'subject': 'Math', 'marks': 90},
     {'name': 'Bob', 'subject': 'Math', 'marks': 85},
     {'name': 'Alice', 'subject': 'Physics', 'marks': 88},
     {'name': 'Bob', 'subject': 'Physics', 'marks': 92},
     {'name': 'Alice', 'subject': 'Chemistry', 'marks': 78},
     {'name': 'Bob', 'subject': 'Chemistry', 'marks': 88}
 ]

highest_scorers = highscore(student_data)
print(highest_scorers)
