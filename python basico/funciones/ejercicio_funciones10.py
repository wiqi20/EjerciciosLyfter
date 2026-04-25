#Cree una función que reciba un string y retorne cuántas vocales contiene
def vowels_counter(my_text):
    counter=0
    vowels="AEIOUaeiou"
    for i in my_text:
        if i in vowels:
            counter+=1
    return(f"el string ingresado contiene {counter} vocales")


print(vowels_counter("hola mundo"))