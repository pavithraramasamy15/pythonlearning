'''
1. with the given input data, create new comn C	
in the dataframe by adding both parallel values 	
of A and B.	
Input:	
data = {'A': [1, 2, 3, 4],	
        'B': [5, 6, 7, 8]}	
	
Output:	
   A  B   C	
0  1  5   6	
1  2  6   8	
2  3  7  10	
3  4  8  12	
	
'''
import pandas as pd 
data = {'A': [1, 2, 3, 4],	
        'B': [5, 6, 7, 8]}	
var=pd.DataFrame(data)
print(var)

var['C']=var['A']+var['B']
print(var)


'''
2. with the given input, find out the values of both A and B of index 2 as shown in given output.	
Input:	
data = {'A': [1, 2, 3, 4],	
        'B': [5, 6, 7, 8]}	
Output:	
A    3	
B    7	
Name: 2, dtype: int64	
'''

import pandas as pd 
data = {'A': [1, 2, 3, 4],	
        'B': [5, 6, 7, 8]}
var=pd.DataFrame(data)
print(var)
print(var.loc[2])

'''
3. Write a function to concatenate both datas horizontally along the columns axis.	
	
Input:	
data1 = {'A': [1, 2, 3, 4],	
         'B': [5, 6, 7, 8]}	
data2 = {'C': [9, 10, 11, 12],	
         'D': [13, 14, 15, 16]}	
	
Expected output:	
   A  B   C   D	
0  1  5   9  13	
1  2  6  10  14	
2  3  7  11  15	
3  4  8  12  16	
 '''
import pandas as pd 
data1 = {'A': [1, 2, 3, 4],	
         'B': [5, 6, 7, 8]}	
data2 = {'C': [9, 10, 11, 12],	
         'D': [13, 14, 15, 16]}	

def concat(data1,data2):
        var=pd.DataFrame(data1)
        var1=pd.DataFrame(data2)
        print(var)
        print(var1)
        res=pd.concat([var,var1],axis=1)
        return res
output=concat(data1,data2)
print(output)
        
'''4. Write a function to create a new column 'Age Group' in the DataFrame df based on the following conditions:    
If Age is less than 30, set 'Age Group' as 'Young'.
If Age is between 30 and 40 (inclusive), set 'Age Group' as 'Adult'.    
If Age is greater than 40, set 'Age Group' as 'Senior'.    
   
Output:
     Name  Age         City Age Group  
0   Alice   25     New York     Young  
1     Bob   30  Los Angeles     Adult  
2  Charlie   35      Chicago     Adult  
3    David   40      Houston     Adult  '''
 
# Pandas.apply allow the users to pass a function and apply it on every single value of the Pandas series.
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],  
        'Age': [25, 30, 35, 40],    
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}  
 
def age_grp(age):
    if age < 30:
        return 'Young'
    elif 30 <= age <= 40:
        return 'Adult'
    elif age > 40:
        return 'Senior'
    else:
        return None
 
def add_age_grp_col(df):
    df['Age Group'] = df['Age'].apply(age_grp)
    return df
 
df = pd.DataFrame(data)
print(add_age_grp_col(df))
 
 
'''5. Write a code snippet to create a new column 'C' in the DataFrame df such that:    
If the value in column 'A' is odd, set 'C' as the value in column 'B' multiplied by 2.  
If the value in column 'A' is even, set 'C' as the square root of the value in column 'B'.  
   
Expected output:    
   A   B     C  
0  1  10    20.
1  2  20   4.472136
2  3  30    60.
3  4  40   6.324555
4  5  50   100. '''
 
import pandas as pd
import numpy as np
 
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]}
 
def odd_even(df):
    if df['A'] % 2 != 0:  #odd
        return '{:.6f}'.format(df['B'] * 2).rstrip('0').rstrip('.')
 
    elif df['A'] % 2 == 0: # even
        return np.sqrt(df['B'])
 
def output(data):
    df = pd.DataFrame(data)
    df['C'] = df.apply(odd_even, axis=1)
    return df
 
print(output(data))
    
'''
# 6. create a csv file using df.to_csv with below data, then handle all null values(np.nan is null value here)
# and replace them with no name avilable, no salary found, department not available , age not found for each column

# Input:
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', '', 'Eva', 'Frank', 'Grace', 'Henry', ''],
#     'Age': [25, np.nan, 35, 40, 28, 33, np.nan, 45, 50, 29],
#     'Salary': [50000, '', 70000, np.nan, 60000, 55000, 65000, np.nan, 75000, 58000],
#     'Department': ['HR', np.nan, 'Sales', '', 'IT', 'HR', 'IT', 'Sales', '', 'HR']
# }

# Expected output:
#        Name   Age             Salary      Department
# 0     ALICE  25.0             50000.0             HR
# 1       BOB  No Age           No salary  No Department
# 2   CHARLIE  35.0             70000.0          Sales
# 3     DAVID  40.0  62333.333333333336  No Department
# 4   NO NAME  28.0               None             IT
# 5       EVA  33.0             55000.0             HR
# 6     FRANK  No Age            65000.0             IT
# 7     GRACE  45.0  
# 8     HENRY  50.0             75000.0  No Department
# 9   NO NAME  29.0             58000.0             HR'''


import pandas as pd
import numpy as np

# Input data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', '', 'Eva', 'Frank', 'Grace', 'Henry', ''],
    'Age': [25, np.nan, 35, 40, 28, 33, np.nan, 45, 50, 29],
    'Salary': [50000, '', 70000, np.nan, 60000, 55000, 65000, np.nan, 75000, 58000],
    'Department': ['HR', np.nan, 'Sales', '', 'IT', 'HR', 'IT', 'Sales', '', 'HR']
}

# Create DataFrame
df = pd.DataFrame(data)

# Define replacement values for nulls
replacement_values = {
    'Name': 'no name available',
    'Age': 'age not found',
    'Salary': 'no salary found',
    'Department': 'department not available'
}

# Replace null values with specified placeholders
df.fillna(replacement_values, inplace=True)
df.replace('', replacement_values, inplace=True)

# Save DataFrame to CSV
df.to_csv('data.csv', index=False)

print("CSV file saved successfully.")






	