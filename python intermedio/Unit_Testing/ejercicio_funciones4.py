#Cree una función que le dé la vuelta a un string y lo retorne.
def inverted_string(my_string):
    new_string=""
    for index in my_string [::-1]: #primer -1 indica que bucle empieza en la ultima posicion, segundo -1 indica que debe ir al indice 0, tercer -1 indica que el incremento es negativo meaning se avanza a la izquierda
        new_string=new_string+index
    return(new_string)


print(inverted_string("hola mundo"))