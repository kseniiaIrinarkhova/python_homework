#import libs
import csv

#Task 2: Read a CSV File

#declare variables
csv_data_dict = dict()
csv_rows = list()

#try to read csv file
try:
    with open('employees.csv', 'r') as file:
        reader = csv.reader(file)
        csv_data_dict['fields'] = next(reader)
        for row in reader:
            csv_rows.append(row)
        csv_data_dict['rows'] = csv_rows
        print(csv_data_dict)
            
except Exception as e:
    print(f'Exception: {e}')
else:
    print(f'Successfully read csv file!')
