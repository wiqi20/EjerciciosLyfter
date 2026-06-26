#Cree un decorador que haga print de los parámetros y retorno de la función que decore.
def print_result(func):
    def wrapper(*args):
        print(f"Parameters: args={args}") #received parameters
        result= func(*args)             #execute the function with the received parameters
        print(f"Result: {result}")
        return result
    return wrapper


@print_result
def function(*numbers): #receive infinite parameters
    print("This is Sum")
    return sum(numbers)


function(10,5,3)