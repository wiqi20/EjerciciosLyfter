import datetime
import functools


def validate_numbers(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in list(args) +list(kwargs.values()):
            if not isinstance(arg,(int,float)):
                raise ValueError(f"({arg}) is not a number, Please enter only numbers")
        return func(*args, **kwargs)
    return wrapper


def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        date= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"funtion name: {func.__name__}")
        print(f"arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Current date: {date}")
        print(f"Return : {result}\n")
        return result
    return wrapper


@log_call
@validate_numbers
def multiply(a,b):
    return a*b


try:
    multiply(5,5)
except Exception as e:
    print("Error:", e)