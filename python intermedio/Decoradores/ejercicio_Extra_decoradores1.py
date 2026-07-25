def repeat_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper


@repeat_twice
def function(text):
    if text:
        print(text)
    return text


function("Hola, Abner")