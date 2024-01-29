#1.Turn every item of a list into its square .Given a list of numbers write a program to turn every item of a list into its square. Try to write it in function using both list comprehension, for loop methods separately.
#Input : numbers = [1, 2, 3, 4, 5] 
#Expected Output : [1, 4, 9, 16, 25]
#USING FOR LOOP:
numbers=[1,2,3,4,5]
newlist=[]
for num in numbers:
    newlist.append(num ** 2)
print(newlist)
#USING LIST COMPREHENSION
newlist = [num ** 2 for num in numbers]
print(newlist)
#USING FUNCTION
def sq_rt(numbers):
    newlist = [num ** 2 for num in numbers]
    return newlist
sq_rt(numbers)
#2) Concatenate two lists in the following order
#Input:
#list1 = ["Hello ", "take"] list2 = ["Dear", "Sir"]
#Output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
list1=["Hello","take"]
list2=["Dear","Sir"] 
list3=[]
for list in list1:
    for words in list2:
        list3.append(list+words)
print(list3) 
#ANOTHER WAY
for list in list1:
    a = str(list) + str(list2[0])
    b = str(list) + str(list2[1])
    list3.append(a)
    list3.append(b)
print(list3)      
#3. Remove empty strings from the list of strings
#Input:    ["Mike", "", "Emma", "Kelly", "", "Brad"]
#output: ['Mike', 'Emma', 'Kelly', 'Brad']

a=["milk","","emma","","kelly","","brad"]
while "" in a:
    a.remove("")
print(a)
#4) Convert two lists into a dictionary
#Input : 
#keys = ['Ten', 'Twenty', 'Thirty'] 
#values = [10, 20, 30]
keys=["ten","twenty","thirty"]
values=[10,20,30]
newlist=dict.fromkeys(keys)
for i in range(len(keys)):
    newlist[keys[i]]=values[i]
print(newlist)
#5)  Delete a list of keys from a dictionary
#Input : 
#sample_dict =          {"name": "Kelly",     "age": 25,     "salary": 8000,     "city": "New York"}
#Output:       {'age': 25, 'city': 'New York'}

sample_dict={"name":"kelly","age":25,"salary":8000,"city":"New York"}
sample_dict.pop("name")
print(sample_dict)



