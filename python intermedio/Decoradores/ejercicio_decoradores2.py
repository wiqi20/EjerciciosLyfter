#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.
def print_result(func):
    def wrapper(*args):
        print(f"Parameters: args={args}") #received parameters
        result= func(*args)             #execute the function with the received parameters
        print(f"Result: {result}")
        return result
    return wrapper


def validate_numbers(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg,(int,float)):
                raise ValueError(f"the entered parameter ({arg}) is not a number")
        return func(*args)          
    return wrapper

@print_result
@validate_numbers
def function(*numbers): #receive infinite parameters
    print("This is Sum")
    return sum(numbers)

try:
    function(10,5,3)
except ValueError as e:
    print("Error:", e)