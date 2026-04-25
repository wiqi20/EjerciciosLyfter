#Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto
def find_character(my_string, my_search):
    counter=0
    for i in my_string:
        if my_search==i:
            counter+=1
    return (f"el carácter {my_search} aparece {counter} veces")


print(find_character("Hola mundo", "o"))