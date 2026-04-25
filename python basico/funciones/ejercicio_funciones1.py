#Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
def funcion1():
    print("Hola ")
    funcion2()


def funcion2():
    print("Mundo")


funcion1()