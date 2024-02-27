# 1.Given a DataFrame containing information about sales transactions, 
# how would you find the total sales amount for each product category where the sales quantity is greater than 100?	
	
# Input:	
# data = {'Product': ['A', 'B', 'A', 'C', 'B', 'C'],	
#         'Quantity': [150, 80, 200, 120, 90, 110],	
#         'Amount': [500, 300, 600, 400, 250, 350]}	
	
# Output:	
#   Product  Total_Sales_Amount	
# 0       A                 1100	
# 1       C                  750

import pandas as pd
data = {'Product': ['A', 'B', 'A', 'C', 'B', 'C'],	
         'Quantity': [150, 80, 200, 120, 90, 110],	
         'Amount': [500, 300, 600, 400, 250, 350]}
df=pd.DataFrame(data)
print(df)
print("\n")

print(type(df))
res=df[df['Quantity'] >100]
print(res)
print("\n")

output=res.groupby('Product')['Amount'].sum().reset_index()
print(output)

print("\n")
print("2 ques \n")

# 2. Given a DataFrame with information about students and their test scores, 
# how would you find the average score for each subject, 
# but only for students who scored above the mean score across all subjects?	
# Input:	
# data = {'Student': ['A', 'B', 'C', 'D', 'E'],	
#         'Math': [80, 70, 90, 60, 85],	
#         'Science': [75, 85, 80, 70, 95],	
#         'English': [65, 75, 70, 80, 90]}	
# Output:	   
#    Subject  Average_Score	
# 0     Math           85.0	
# 1  Science           85.0	
# 2  English           85.0	

import pandas as pd
data={'Student': ['A', 'B', 'C', 'D', 'E'],	
        'Math': [80, 70, 90, 60, 85],	
         'Science': [75, 85, 80, 70, 95],	
        'English': [65, 75, 70, 80, 90]}
df=pd.DataFrame(data)
print(df)
print("\n")
mean_all_subjects = df[['Math', 'Science', 'English']].values.mean()
print(mean_all_subjects)
print("\n")

df_above_mean = df[df[['Math', 'Science', 'English']].mean(axis=1) > mean_all_subjects]
print(df_above_mean)
print("\n")


average_scores = df_above_mean[['Math', 'Science', 'English']].mean()
print(average_scores)
print("\n")


output_df = pd.DataFrame({'Subject': average_scores.index, 'Average_Score': average_scores.values})

print(output_df)
print("\n")
print("3 ques \n")

# 3. Given a DataFrame with a time series index and a column representing stock prices, 
# how would you identify the dates where the stock price increased by more than 10% compared to the previous day? (go through some timeseries topics in pandas) 	
# Input:	
# prices = [100, 110, 105, 120, 130, 115, 112, 125, 130, 135]	
# Output:	
#           Price	
# 2024-01-02    110	
# 2024-01-04    120	
# 2024-01-05    130	
# 2024-01-10    135	


import pandas as pd
from datetime import datetime
dates=pd.date_range(start='2024-01-01', periods=10, freq='D')
prices = [100, 110, 105, 120, 130, 115, 112, 125, 130, 135]
df=pd.DataFrame(prices,index=dates,columns=['StockPrice'])
print(df)
print("\n")

df['Percentage Change'] = df['StockPrice'].pct_change() * 100
# pc=df['StockPrice'].pct_change() * 100
# print(pc)
increased_percent = df[df['Percentage Change'] > 10]
print(increased_percent)
print("\n")
# increased_by_10_percent.drop(columns=['Percentage Change'], inplace=True)
# print(increased_by_10_percent)
print("4 ques \n")

# 4.Given a DataFrame with information about sales transactions and another DataFrame with information about discounts, 
# how would you calculate the total discounted amount for each product sold, considering both the quantity and discount rate?	
# Input:	
# sales_data = {'Product': ['A', 'B', 'A', 'C', 'B', 'C'],	
#               'Quantity': [10, 20, 30, 40, 50, 60],	
#               'Amount': [500, 600, 700, 800, 900, 1000]}	
	
# discount_data = {'Product': ['A', 'B', 'C'],	
#                  'Discount_Rate': [0.1, 0.2, 0.15]}	
# Output:	
#   Product  Total_Discounted_Amount	
# 0       A                     500	
# 1       B                    1000	
# 2       C                    1900	
sales_data={'Product': ['A', 'B', 'A', 'C', 'B', 'C'],	
              'Quantity': [10, 20, 30, 40, 50, 60],	
              'Amount': [500, 600, 700, 800, 900, 1000]}
discount_data = {'Product': ['A', 'B', 'C'],	
                 'Discount_Rate': [0.1, 0.2, 0.15]}

import pandas as pd

sales_df = pd.DataFrame(sales_data)
print("sales_df \n")
print(sales_df)
print("\n")

discount_df = pd.DataFrame(discount_data)
print("discount_df:\n")
print(discount_df)
print("\n")

merged_df = pd.merge(sales_df, discount_df, on='Product', how='left')
print("merged_df:\n")
print(merged_df)
print("\n")

merged_df['Discounted_Amount'] = merged_df['Amount'] * merged_df['Discount_Rate'] * merged_df['Quantity']
print("Discount_Amount: \n\n", merged_df)
total_discounted_amount = merged_df.groupby('Product')['Discounted_Amount'].sum().reset_index()
print( total_discounted_amount)
print("\n")
# total_discounted_amount.columns = ['Product', 'Total_Discounted_Amount']
# print(total_discounted_amount)
print("5 ques \n")

# 5. Given a DataFrame with information about customer orders, 
# how would you find the total number of orders placed by customers who have made more than one order?	
	
# Input:	
# data = {'Customer': ['A', 'B', 'A', 'C', 'B', 'C'],	
#         'Order_ID': [1, 2, 3, 4, 5, 6]}	
	
# Output:	
#   Total_Orders	
# 0             3
import pandas as pd
data={'Customer': ['A', 'B', 'A', 'C', 'B', 'C'],	
        'Order_ID': [1, 2, 3, 4, 5, 6]}
df=pd.DataFrame(data)
print(df)
print("\n")
count_order=df.groupby('Customer')['Order_ID'].count()
print(count_order)
print("\n")
total_order=count_order[count_order >1]
result=total_order.count()
output=pd.DataFrame({'Total_orders':[result]})
print(output)
print("\n")
print("6 ques \n")

# 6.  Given a DataFrame with a column containing JSON strings representing nested data, 
# how would you extract a specific value nested within the JSON for each row?	
	
# Input:	
# data = {'ID': [1, 2, 3],	
#         'Nested_Data': ['{"key1": {"key2": {"key3": 10}}}',	
#                         '{"key1": {"key2": {"key3": 20}}}',	
#                         '{"key1": {"key2": {"key3": 30}}}']}	
# Output:	
# ID  Nested_Value	
# 0 1 10	
# 1 2 20	
# 2 3 30

import pandas as pd
import json


data = {
    'ID': [1, 2, 3],
    'Nested_Data': ['{"key1": {"key2": {"key3": 10}}}',
                    '{"key1": {"key2": {"key3": 20}}}',
                    '{"key1": {"key2": {"key3": 30}}}'
                   ]
}

df = pd.DataFrame(data)
print(df)
print("\n")

def extract_nested_value(json_str):
    nested_data = json.loads(json_str)
    return nested_data['key1']['key2']['key3']

df['Nested_Value'] = df['Nested_Data'].apply(extract_nested_value)


print(df[['ID', 'Nested_Value']])
print("\n")
print("7 ques \n")

# 7.  Given a DataFrame with duplicate rows,
# how would you remove the duplicate rows based on a subset of columns while keeping only the row with the maximum value in another column?	
	
# Input:	
# data = {'ID': [1, 1, 2, 2, 3],	
#         'Value': [10, 20, 30, 40, 50],	
#         'Timestamp': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03']}	
	
# Output:	
#    ID  Value   Timestamp	
# 1   1     20  2024-01-01	
# 3   2     40  2024-01-02	
# 4   3     50  2024-01-03	

import pandas as pd
data = {'ID': [1, 1, 2, 2, 3],	
        'Value': [10, 20, 30, 40, 50],	
        'Timestamp': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03']}
df=pd.DataFrame(data)
print(df)
print("\n")

res=df.drop_duplicates(subset='ID',keep='last')

# res = df.loc[df.groupby('ID')['Value'].idxmax()
# res = df.loc[df.groupby('ID')['Value'].idxmax()]

print(res)
print("\n")










	
	