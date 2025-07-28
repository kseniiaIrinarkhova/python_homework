#import libs
import csv
import traceback

#Task 2: Read a CSV File

global employees

#function that read csv file and returned employees data
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

employees = read_employees()
print(f"{employees} len={len(employees)}")