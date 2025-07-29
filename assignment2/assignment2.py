#import libs
import csv
import traceback
import os
import custom_module
from datetime import datetime


#global variables:
global employees
global employee_id_column
global minutes_set
global minutes_list

#Helper functions

#function that read csv file and return dictionary of headets and rows
#file_path:string - path to CSV file
#convert_to_tulple:boolean - flag that emphasize that need convertion of row data to tuple. By defaule - false 
def read_file(file_path, convert_to_tulple=False):
    #declare variables
    csv_data_dict = dict()
    csv_rows = list()

    #try to read csv file
    try:
        #open file for reading
        with open(file_path, 'r') as file:
            # create reader object
            reader = csv.reader(file)
            #get 1st line and save it to dictionary as headers
            csv_data_dict['fields'] = next(reader)
            #loop through rows and add them to list
            for row in reader:
                if(convert_to_tulple):
                    csv_rows.append(tuple(row))
                else:
                    csv_rows.append(row)
            #add list to dictionary
            csv_data_dict['rows'] = csv_rows
            #return data
            return csv_data_dict            
    except Exception as e:
        #print type of exception
        print(f"An exception occurred {type(e).__name__}")
        # get and print exception message
        message = str(e)
        if message:
            print(f'Exception message: {message}')
        #trace back exception
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        #create a stack of commands
        for trace in trace_back:
            stack_trace.append(f'File: {trace[0]}, Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        #print stack of commands from exception
        print(f"Stack trace: {stack_trace}")

#Task 2: Read a CSV File

#function that read csv file and returned employees data
#return - dictionary of data from csv file:
#{
#[Key: fields]: list()
#[Key: rows]: list()
#}
def read_employees():
    return read_file('../csv/employees.csv')

#test the output
employees = read_employees()
# print(f"{employees} len={len(employees)}")

#Task 3: Find the Column Index

#function for getting column index
#field_name:string - name of the field 
#retun - index of column
def column_index(field_name):
    try:
        return employees["fields"].index(field_name)
    except Exception as e:
        #print type of exception
        print(f"An exception occurred {type(e).__name__}")
        # get and print exception message
        message = str(e)
        if message:
            print(f'Exception message: {message}')
        #trace back exception
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        #create a stack of commands
        for trace in trace_back:
            stack_trace.append(f'File: {trace[0]}, Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        #print stack of commands from exception
        print(f"Stack trace: {stack_trace}")

#test the output
# print(f"{column_index("employee_desc")}")
employee_id_column = column_index("employee_id")
# print(f'{employee_id_column}')

#Task 4: Find the Employee First Name

#function to get first name from specific row
#row_number:number - number of the row to fetch data
#return: string - first name
def first_name(row_number):
    #find the index of "first name" column
    first_name_index = column_index("first_name")
    try:
        return employees["rows"][row_number][first_name_index]
    except Exception as e:
        #print type of exception
        print(f"An exception occurred {type(e).__name__}")
        # get and print exception message
        message = str(e)
        if message:
            print(f'Exception message: {message}')
        #trace back exception
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        #create a stack of commands
        for trace in trace_back:
            stack_trace.append(f'File: {trace[0]}, Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        #print stack of commands from exception
        print(f"Stack trace: {stack_trace}")

#check output
# print(f'{first_name(1)}')
# print(f'{first_name("2")}')
# print(f'{first_name("third")}')

# Task 5: Find the Employee: a Function in a Function

#function that returns employees by id
#employee_id:int - employee ID
#return: list - list of employees with id == employee_id 
def employee_find(employee_id):
    try:
        #comparison function
        def employee_match(row):
            return int(row[employee_id_column]) == employee_id
        #filter employee from rows data by id
        matches = list(filter(employee_match, employees["rows"]))
        return matches
    except Exception as e:
        #print type of exception
        print(f"An exception occurred {type(e).__name__}")
        # get and print exception message
        message = str(e)
        if message:
            print(f'Exception message: {message}')
        #trace back exception
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        #create a stack of commands
        for trace in trace_back:
            stack_trace.append(f'File: {trace[0]}, Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        #print stack of commands from exception
        print(f"Stack trace: {stack_trace}")

# print(f'{employee_find(3)}')
# print(f'{employee_find("2")}')
    
#Task 6: Find the Employee with a Lambda

#function that returns employees by id
#employee_id:int - employee ID
#return: list - list of employees with id == employee_id 
def employee_find_2(employee_id):
     #filter employees["rows"] list with lambda function by id
     matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
     return matches

# print(f'{employee_find_2(3)}')
# print(f'{employee_find_2("2")}')

#Task 7: Sort the Rows by last_name Using a Lambda

#function that sort data by last name column
def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]

# print(employees["rows"])
# print(f'{sort_by_last_name()}')

#Task 8: Create a dict for an Employee

# #function that create employee object
# #data:list - row from csv file
# #return:dictionary object - employee
# def employee_dict(data):
#     #declare employee object
#     employee = dict()
#     #loop through data, except employee_id, which is 0 index
#     for index in range(1, len(employees["fields"])):
#         #add data to object
#         employee[employees["fields"][index]] = data[index]
#     return employee

#function that create employee object with zip
#data:list - row from csv file
#return:dictionary object - employee
def employee_dict(data):
    #declare employee object using zip function
    employee = dict(zip(employees["fields"], data))
    #delete emplotee_id key
    del employee["employee_id"]
    return employee

#print result
# print(f'{employee_dict(employees["rows"][5])}')

#Task 9: A dict of dicts, for All Employees

#function that created dictionary for all employees
#return: dictionary
#[key:employee_id]: value - dict()employee data
def all_employees_dict():
    #declare dictionary for employees
    employees_dict = dict()
    #loop through rows
    for row in employees["rows"]:
        #create employee entry
        employees_dict[row[0]] = employee_dict(row)
    return employees_dict

#print result
# print(f'{all_employees_dict()}')

#Task 10: Use the os Module
#function that read THISVALUE env variable
def get_this_value():
    return os.getenv("THISVALUE")

#print result
# print(f"{get_this_value()}")

#Task 11: Creating Your Own Module

#function that set secret from custom module
#secret_data:string - data that would be set for secret
def set_that_secret(secret_data):
    custom_module.set_secret(secret_data)

# set_that_secret("I could change you if I know you!")
# print(f"{custom_module.secret}")

#Task 12: Read minutes1.csv and minutes2.csv

#function that read minutes files and return data as dictionary with tuples
def read_minutes():
    #read minutes1.csv
    minutes1 = read_file("../csv/minutes1.csv", True)
    #read minutes2.csv
    minutes2 = read_file("../csv/minutes2.csv", True)
    return minutes1, minutes2

#check the result
minutes1, minutes2 = read_minutes()
# print(f"Minutes1 = {minutes1} \n\r Minutes2 = {minutes2}")

#Task 13: Create minutes_set

#function that create union set from 2 lists of minutes data
def create_minutes_set():
    #read lists of data from files
    minutes1, minutes2 = read_minutes()
    #create set from 1st list
    min1_set = set(minutes1["rows"])
    #create set from 2nd list
    min2_set = set(minutes2["rows"])
    #return union of 2 sets
    return min1_set.union(min2_set)

minutes_set = create_minutes_set()
# print(f"in minutes1 = {len(minutes1["rows"])}, in minutes2 = {len(minutes2["rows"])}, in union set = {len(minutes_set)} \n\r {minutes_set}")

#Task 14: Convert to datetime

def create_minutes_list():
    minutes_list = list(minutes_set)
    converted_minutes = list(map(lambda row: (row[0], datetime.strptime(row[1], "%B %d, %Y") ), minutes_list))
    return converted_minutes

minutes_list = create_minutes_list()
print(f"{minutes_list}")

