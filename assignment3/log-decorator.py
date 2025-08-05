#import libs
import logging

#Task 1: Writing and Testing a Decorator

#decorator functtion to log functions call
def logger_decorator(func):
    #wrapper to have access to function parameters
    def wrapper(*args, **kwargs):
        #set up logger
        logger = logging.getLogger(__name__ + '_parameter_log')
        logger.setLevel(logging.INFO)
        #check for existing file handlers
        if not logger.handlers:
            logger.addHandler(logging.FileHandler(".decorator.log",'a'))
        #get function result
        value = func(*args, **kwargs)
        #create a log data
        log = f"Function: {func.__name__}, *args {args}, **kwargs {kwargs}, return: {value}"
        #log data to file
        logger.log(logging.INFO, log)
        #return function result
        return value
    return wrapper

#simple function without parameters and return
@logger_decorator
def greeting():
    print('Hello World!')

#function with variable number of positional arguments and value in return
@logger_decorator
def sum_numbers(*numbers):
    result = sum(numbers)
    print(f"Numbers: {numbers}, and sum: {result}")
    return True

#function with variable number of keyword arguments and function as return
@logger_decorator
def describe_cat(**details):
    cat = dict()
    for key,value in details.items():
        # print(f"{key}:{value}")
        cat[key] = value
    print(cat)
    return logger_decorator

#check the result
greeting()
sum_numbers(1,2,3,4)
describe_cat(name='Chicory', breed="maine coon", age="5", color="black")
