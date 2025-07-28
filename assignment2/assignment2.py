#import libs
import csv
import traceback

#global variables:
global employees
global employee_id_column

#Task 2: Read a CSV File

#function that read csv file and returned employees data
#return - dictionary of data from csv file:
#{
#[Key: fields]: list()
#[Key: rows]: list()
#}
def read_employees():
    #declare variables
    csv_data_dict = dict()
    csv_rows = list()

    #try to read csv file
    try:
        #open file for reading
        with open('../csv/employees.csv', 'r') as file:
            # create reader object
            reader = csv.reader(file)
            #get 1st line and save it to dictionary as headers
            csv_data_dict['fields'] = next(reader)
            #loop through rows and add them to list
            for row in reader:
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
print(f"{column_index("employee_desc")}")
employee_id_column = column_index("employee_id")
print(f'{employee_id_column}')

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
print(f'{first_name(1)}')
print(f'{first_name("2")}')
print(f'{first_name("third")}')