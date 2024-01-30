#1.Develop a Python program to create a dictionary from a given string, where each key represents a unique character, and the corresponding values denote the count of occurrences.
#Input: 'kovan labs'
#Output: {'k': 1, 'o': 1, 'v': 1, 'a': 2, 'n': 1, ' ': 1, 'l': 1, 'b': 1, 's': 1}

inputs="Kovan labs"
newdict=dict.fromkeys(inputs)
for i in inputs:    
    newdict[i]=inputs.count("Kovan labs")
print(newdict)

inputs="kovan labs"
newset={}
for i in inputs:
    if i in newset:
        newset[i] +=1
    else:
        newset[i]=1
print(str(newset))
     
#2. Create a Python program to find the key with the maximum value in a dictionary.
#Input: 
#my_dict = {'apple': 10, 'banana': 5, 'orange': 20, 'grapes': 15}
#Output: 'orange'

my_dict={"apple" : 10,"banana": 5,"orange" : 20,"grapes" : 15}
v=list(my_dict.values())
k=list(my_dict.keys())
print(v)
print(k)
print(k[v.index(max(v))])

#3.Create a Python function that counts the frequency of words in a sentence and returns a dictionary.
#Input: 
#sentence = "This is a sample sentence. This sentence has words."
#Output: {'This': 2, 'is': 1, 'a': 1, 'sample': 1, 'sentence.': 2, 'has': 1, 'words.': 1}

sentence ="This is a sample sentence. This sentence has words."
newset={}
x=sentence.split()
for i in x:
    if i in newset:
        newset[i]+=1
    else:
        newset[i]=1
print(str(newset))

#4.  Write a Python function that takes a dictionary as input and returns a new dictionary where the keys are the original values, and the values are lists containing all corresponding keys.
#Input: 
#input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}
#Output: {1: ['a', 'c'], 2: ['b', 'd'], 3: ['e']}

input_dict ={'a':1,'b':2,'c':1,'d':2,'e':3}
emp_list=[]
def fun_dict(input_dict):
    for key,value in input_dict.items():
        if value not in emp_list:
            emp_list[value]=[key]
        else:
            emp_list[value].append(key)
    return emp_list
fun_dict(input_dict)

    



    
    
    
    








    

 
    
    



    
    
    
    















    