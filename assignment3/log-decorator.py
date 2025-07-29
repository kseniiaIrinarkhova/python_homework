#import libs
import logging

#Task 1: Writing and Testing a Decorator

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(__name__ + '_parameter_log')
        logger.setLevel(logging.INFO)
        logger.addHandler(logging.FileHandler(".decorator.log",'a'))
        value = func(*args, **kwargs)
        logger.log(logging.INFO, func.__name__)
        return value
    return wrapper

@logger_decorator
def greeting():
    print('Hello World!')

greeting()