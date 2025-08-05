#import libs
import csv

#Task 3: List Comprehensions Practice

#declare variables
csv_rows = list()

#try to read csv file
try:
    #open file for reading
    with open('../csv/employees.csv', 'r') as file:
        # create reader object
        reader = csv.reader(file)
        #create a list of lists
        csv_rows = [row for row in reader]                 
except Exception as e:
    #print type of exception
    print(f"An exception occurred {type(e).__name__}")
    # get and print exception message
    message = str(e)
    if message:
        print(f'Exception message: {message}')

print('------------Full list of employees----------------------------')
print(csv_rows)

employee_names = [f'{employee[1]} {employee[2]}' for index, employee in enumerate(csv_rows) if index != 0]

print("------------Only employees names-------------------------------")
print( employee_names)

filtered_employees = [employee for employee in employee_names if employee.find('e') != -1]

print("------------Only employees with 'e' letter in name------------")
print(filtered_employees)
