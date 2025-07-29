#import libs
import logging

#Task 1: Writing and Testing a Decorator

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(__name__ + '_parameter_log')
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            logger.addHandler(logging.FileHandler(".decorator.log",'a'))
        value = func(*args, **kwargs)
        log = f"Function: {func.__name__}, *args {args}, **kwargs {kwargs}, return: {value}"
        logger.log(logging.INFO, log)
        return value
    return wrapper

@logger_decorator
def greeting():
    print('Hello World!')

@logger_decorator
def sum_numbers(*numbers):
    result = sum(numbers)
    print(f"Numbers: {numbers}, and sum: {result}")
    return True

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
