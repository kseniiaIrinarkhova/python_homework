#import libs and frameworks
import pandas as pd
from dateutil import parser

#additional data
UNKNOWN = ["unknown", "NaN", "n/a"]

#helper function to parce the dates
def parse_date_safe(date_str):
    try:
        return parser.parse(date_str, dayfirst=True)  
    except (ValueError, TypeError):
        return pd.NaT

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

#Task 2: Loading Data from CSV and JSON

#read the data from CSV
task2_employees = pd.read_csv('employees.csv')
# print(task2_employees)

#read the data from json file
json_employees = pd.read_json('additional_employees.json')
# print(json_employees )

#combine CSV and JSON data
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)

# print(more_employees)

#Task 3: Data Inspection - Using Head, Tail, and Info Methods

#get top 3 employees from DataFrame
first_three = more_employees.head(3)
# print(first_three)

##get last 2 employees
last_two = more_employees.tail(2)
# print(last_two)

#get shape of DataFrame
employee_shape = more_employees.shape
# print(employee_shape)

#use info method
# more_employees.info()

#Task 4: Data Cleaning

#read dirty data from CSV
dirty_data = pd.read_csv('dirty_data.csv')
# print(dirty_data)

#make a copy of data
clean_data = dirty_data.copy()
#delete duplicates
clean_data = clean_data.drop_duplicates()
#clean Age column
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
#clean Salary column
clean_data["Salary"] = pd.to_numeric(clean_data['Salary'], errors='coerce')

#fill the missing data
mean_age = clean_data['Age'].mean()
clean_data['Age']  = clean_data['Age'].fillna(mean_age)
median_salary = clean_data['Salary'].median()
clean_data['Salary'] = clean_data['Salary'].fillna(median_salary)

#convert hire date to datatime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')

#Text Standardization
#strip whitespace
clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Department'] = clean_data['Department'].str.strip()
#convert columns to uppercase
clean_data['Name'] = clean_data['Name'].str.upper()
clean_data['Department'] = clean_data['Department'].str.upper()

#convert NaT Hire Dates
dirty_dates = dirty_data['Hire Date'].copy()
clean_dates = dirty_dates.apply(parse_date_safe) #use dateutil parser because it is more flexible

clean_data['Hire Date'] = clean_dates

print(clean_data)
