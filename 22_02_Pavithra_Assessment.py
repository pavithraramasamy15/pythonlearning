# 1. Consider the following data as dataframe.

# Input:
# data = {'Text': ['Hello world', 'Python is awesome', 'Data science is fun']}

# a) What code should you use to add a new column named Word_Count to df which contains the number of words in each text entry?

# Expected Output:
#        Text  Word_Count
# 0  Hello world           2
# 1 Python is awesome     3
# 2 Data science is fun   4

import pandas as pd
data = {'Text': ['Hello world', 'Python is awesome', 'Data science is fun']}
df=pd.DataFrame(data)
print(type(df))
                           
# USING STR SPLIT AND STR LEN
df["Word_count"]=df["Text"].str.split().str.len()
print(df)
# USING .APPLY()
# df['Word_count'] = df['Text'].apply(lambda x: len(x.split()))
print(df)

# USING STR COUNT()
df['Word_Count'] = df['Text'].str.count(' ') + 1
print(df)

# USING lIST_COMPREHENSION

df['totalwords'] = [len(x.split()) for x in df['Text'].tolist()]
print(df)

# b) Write code to find the most common word in the 'Text' column.	
	
# Expected Output:	
# is'

import pandas as pd
data = {'Text': ['Hello world', 'Python is awesome', 'Data science is fun']}
df=pd.DataFrame(data)
print(df)
text=''.join(df['Text'])
print(text)
word=text.split()
print(word)
s=pd.Series(word)
print(s)
counts=s.value_counts()
print(counts)
maximum=counts.idxmax()
print(maximum)

# c) Write code to replace each word in the 'Text' column with its length. 
# For example, in given input 1st index is Hello WOrld, both words has 5 letters, so it is replaced with 5, 5 in 1st index in below output.	
	
# Expected Output:	
#                    Text	
# 0             5 5	
# 1        6 2 7	
# 2  4 7 2 5 2 3	

import pandas as pd
data = {'Text': ['Hello world', 'Python is awesome', 'Data science is fun']}
df=pd.DataFrame(data)
print(df)

def word_length(text):
    return [len(word) for word in text.split()]
df['Text'] = df['Text'].apply(word_length)
print(df)

# 2. Write code to find the count of individuals in each department.			
			
# Input:			
# data = {'ID': [1, 2, 3, 4, 5],			
#         'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],			
#         'Age': [25, 30, 35, 40, 45],			
#         'Department': ['Sales', 'Marketing', 'Sales', 'HR', 'Marketing']}			
			
# Expected Output:			
# Marketing    2			
# Sales        2			
# HR           1			
# Name: Department, dtype: int64	

import pandas as pd
data = {'ID': [1, 2, 3, 4, 5],			
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],			
        'Age': [25, 30, 35, 40, 45],			
        'Department': ['Sales', 'Marketing', 'Sales', 'HR', 'Marketing']}	
df=pd.DataFrame(data)	
print(df)	
dept_count=df['Department'].value_counts()
print(dept_count)

# 3. You're provided with a dataset containing information about hotel bookings. 
# The dataset includes categorical columns for "Hotel_Name", "Booking_Status", and "Payment_Method".
# Your task is to analyze the booking status distribution for each hotel, focusing on payments made through credit cards. 
# Write a Python function to achieve this.			
			
# Input:			
# data = {			
#     'Hotel_Name': ['Hotel A', 'Hotel B', 'Hotel A', 'Hotel B', 'Hotel A', 'Hotel B'],			
#     'Booking_Status': ['Confirmed', 'Cancelled', 'Confirmed', 'Confirmed', 'Cancelled', 'Confirmed'],			
#     'Payment_Method': ['Credit Card', 'Debit Card', 'Credit Card', 'Credit Card', 'Credit Card', 'Debit Card']			
# }			
			
# Output:			
#   Hotel_Name Booking_Status  Count			
# 0    Hotel A      Cancelled      1			
# 1    Hotel A      Confirmed      2			
# 2    Hotel B      Confirmed      1

import pandas as pd
data = {			
    'Hotel_Name': ['Hotel A', 'Hotel B', 'Hotel A', 'Hotel B', 'Hotel A', 'Hotel B'],			
     'Booking_Status': ['Confirmed', 'Cancelled', 'Confirmed', 'Confirmed', 'Cancelled', 'Confirmed'],			
    'Payment_Method': ['Credit Card', 'Debit Card', 'Credit Card', 'Credit Card', 'Credit Card', 'Debit Card']			
}
df=pd.DataFrame(data)
print(df)
hotel=df[df['Payment_Method']== 'Credit Card']
print(hotel)
hotel_count=hotel.groupby(['Hotel_Name','Booking_Status']).count().reset_index()
print(hotel_count)

# 4. You've been given a dataset containing information about electrical appliances in a store. 
# The dataset includes categorical columns for "Appliance_Name", "Type", and "Availability". 
# Your task is to create a dictionary where each key is an appliance type and the corresponding value is a list containing the names of appliances belonging to that type along with their availability status. 
# Write a Python function to accomplish this.			
# Use pandas.			
			
# Input:			
# data = {			
#     'Appliance_Name': ['Refrigerator', 'Microwave', 'Dishwasher', 'Vacuum Cleaner', 'Toaster', 'Blender'],			
#     'Type': ['Large Appliance', 'Small Appliance', 'Large Appliance', 'Small Appliance', 'Small Appliance', 'Small Appliance'],			
#     'Availability': ['In Stock', 'Out of Stock', 'In Stock', 'Out of Stock', 'In Stock', 'Out of Stock']			
# }			
			
# Expected Output:			
# {			
#     'Large Appliance': [('Refrigerator', 'In Stock'), ('Dishwasher', 'In Stock')],			
#     'Small Appliance': [('Microwave', 'Out of Stock'), ('Vacuum Cleaner', 'Out of Stock'), ('Toaster', 'In Stock'), ('Blender', 'Out of Stock')]			

					
import pandas as pd

data = {            
    'Appliance_Name': ['Refrigerator', 'Microwave', 'Dishwasher', 'Vacuum Cleaner', 'Toaster', 'Blender'],            
    'Type': ['Large Appliance', 'Small Appliance', 'Large Appliance', 'Small Appliance', 'Small Appliance', 'Small Appliance'],            
    'Availability': ['In Stock', 'Out of Stock', 'In Stock', 'Out of Stock', 'In Stock', 'Out of Stock']            
}

df = pd.DataFrame(data)
print(df)
result_dict={}

grouped = df.groupby('Type')
print(grouped)

for name, group in grouped:

    tuples = list(zip(group['Appliance_Name'], group['Availability']))
    print(tuples)
    
    result_dict[name] = tuples
print(result_dict)

    
    





		



    

	


