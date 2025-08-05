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
print(task1_data_frame)

