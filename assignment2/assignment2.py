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
        for row in reader:
            print(row)
except Exception as e:
    print(f'Exception: {e}')
else:
    print(f'Successfully read csv file!')
