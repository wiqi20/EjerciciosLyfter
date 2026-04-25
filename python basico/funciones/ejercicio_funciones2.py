#Experimente con el concepto de scope:
#Intente acceder a una variable definida dentro de una función desde afuera.
#Intente acceder a una variable global desde una función y cambiar su valor.
variable_global="esta es una variable global"
def funcion1():
    variable_local="esta es una variable local"
    global variable_global
    variable_global=variable_global+" modificada"
    print(variable_global)


#print(variable_local)
funcion1()