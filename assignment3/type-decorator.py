#Task 2: A Decorator that Takes an Argument

#decorator factory
def type_converter(type_of_output):
    def decorator(func): #decorator that take function
        def wrapper(*args, **kwargs):  # wrapper: runs the function with extra behavior
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

@type_converter(str)
def return_int():
    return 5

@type_converter(int)
def return_string():
    return 'not a number'

@type_converter(int)
def return_string2():
    return '5'



#check the results
print(f"return_int() result = {return_int()}")
print(f"return_int() result type = {type(return_int()).__name__}")
try:
    y = return_string()
    print("shouldn't get here!")
    print(f"return_string() result type = {y}")
    print(f"return_string() result type = {type(y).__name__}")
except ValueError:
    print("can't convert that string to an integer!")

try:
    y = return_string2()
    print(f"return_string2() result type = {y}")
    print(f"return_string2() result type = {type(y).__name__}")
except ValueError:
    print("can't convert that string to an integer!")