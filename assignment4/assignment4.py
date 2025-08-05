#import libs and frameworks
import pandas as pd

#Task 1: Introduction to Pandas - Creating and Manipulating DataFrames

#create a dictionary
data = {
    'Name':['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

#convert dictionary to DataFrame
task1_data_frame = pd.DataFrame(data)

#check data: 
# print(task1_data_frame)

#make a copy of data
task1_with_salary = task1_data_frame.copy()

#add new column
task1_with_salary['Salary'] = [70000, 80000, 90000]

#check data: 
# print(task1_with_salary)

#make a copy of tasl DataFrame
task1_older= task1_with_salary.copy()

#Create a Series from 'Age' column and increase value by 1
age_series = task1_older['Age'].copy() +1
#change the column in dataFrame using new series
task1_older['Age'] = age_series

#check data: 
# print("DataFrame with increased age")
# print(task1_older)

#save to CSV

# task1_older.to_csv('employees.csv', sep=',', index=False)


