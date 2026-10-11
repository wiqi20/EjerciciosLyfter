#Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
#Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#“python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
def string_to_list(my_string):
    new_list=sorted(my_string.split("-"))
    sorted_string="-".join(new_list)
    return(sorted_string)


print(string_to_list("python-variable-funcion-computadora-monitor"))