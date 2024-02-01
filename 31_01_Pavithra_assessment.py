#1. Write a program to iterate the first 5 numbers, and in each iteration, print the sum of the current and previous number at the end.
#Expected Output:
#Current Number 0 Previous Number  0  Sum:  0
#Current Number 1 Previous Number  0  Sum:  1
#Current Number 2 Previous Number  1  Sum:  3
#Current Number 3 Previous Number  2  Sum:  5
#Current Number 4 Previous Number  3  Sum:  7

num=list(range(5))   #[0,1,2,3,4]
previous_number=0
for i in num:
    sum=previous_number+i
    print("Current Number " + str(i) +" Previous Number " + str(previous_number) + " is " + "Sum: " + str(sum))
    previous_number=i

#2. Write a Program to extract each digit from an integer in the reverse order.For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

num1=7536
str_con = str(num1)
rev=str_con[::-1]
print(rev.replace(""," "))

# #another way
result="".join(reversed(str(num1)))
print(str(result.replace(""," ")))

# 3. Create a list by picking an odd-index items from the first list and even index items from the second
# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.
# Input:
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# Output:
# Element at odd-index positions from list one
# [6, 12, 18]
# Element at even-index positions from list two
# [4, 12, 20, 28]
# Printing Final third list
# [6, 12, 18, 4, 12, 20, 28]

l1=[3,6,9,12,15,18,21]
l2=[4,8,12,16,20,24,28]
oddvalue=l1[1::2]
evenvalue=l2[::2]
l3=oddvalue+evenvalue
print(oddvalue)
print(evenvalue)
print(l3)



#4. Find words with both alphabets and numbers
#Write a program to find words with both alphabets and numbers from an input string.
#Input:
#str1 = "Emma25 is Data scientist50 and AI Expert"
#Output:
#Emma25
#scientist50

def alphaandnum(str1):
    strings=str1.split()
    print(strings)
    result=[]
    for strs in strings:
        if any(c.isalpha() for c in strs) and any(c.isdigit() for c in strs):
            result.append(strs)
    return result
    

str1 = "Emma25 is Data scientist50 and AI Expert"

print(alphaandnum(str1))

#5. Write a Python program to find the second maximum and second minimum elements in a given list of numbers. Assume that the list has at least two distinct elements.
# Input:
# [55, 23, 78, 12, 67, 34, 89, 9, 43]
#  Output:
# Second Maximum: 78
# Second Minimum: 12

list_1=[55,23,78,12,67,34,89,9,43]
list_1.sort()
print(list_1)
print("Second Maximum: ",list_1[-2])
print("Second Minimum: ",list_1[1])


#anotherway

def maxandmin(list_1):
    unique_num=list(set(list_1))
    
    if len(unique_num) < 2:
        print("This list must contain atleast two distinct elements ")
        return 
    
    min_value=min(unique_num)
    max_value=max(unique_num)
    second_min=(min(x for x in unique_num if x != min_value))
    second_max = max(x for x in unique_num if x != max_value)
    print("Second Minimum:", second_min)
    print("Second Maximum:", second_max)
list_1=[55,23,78,12,67,34,89,9,43]
maxandmin(list_1)

    







    
        
        
        
 
