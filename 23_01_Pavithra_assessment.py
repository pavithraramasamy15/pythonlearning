#1)Write a code that takes a string as input and returns the reversed version of that string. For example expected output should be like reversed_output = "nohtyp"
input="python"[::-1]
print(input)

#2)Given two different lists and tuples, write a Python code to merge these two different lists and tuples and store the result in a new items called "combined_list." for each, expected output should be in combined lists and combined tuple format.
#list
list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
combined_list=list1.extend(list2)
combined_list=list1
print(combined_list)
#tuple
tuple1=(1,2,3,4,5)
tuple2=('a','b','c','d','e')
combined_tuple=tuple1+tuple2
print(combined_tuple)

#3)Write a code that takes a string and a target substring as input and returns the number of occurrences of the target substring in the given string. For example, if the input is "pythonpythonpython" and the target substring is "on," the output should be 3
string="pythonpythonpython"
num_occur=string.count("on")
print(num_occur)

#4)write a python code to achieve the expected output below mentioned
#text  = "#orange#strawberry#grapes#banana"
#result = ['orange', 'strawberry', 'grapes', 'banana']
text="#orange#strawberry#grapes#banana"
result=text.split("#")
print(t)




