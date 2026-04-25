#Cree un programa que elimine todos los números impares de una lista.
#Ejemplos: my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] → [2, 4, 6, 8]
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for index in range(len(my_list)-1,-1,-1): #primer -1 indica que bucle empieza en la ultima posicion, segundo -1 indica que debe ir al indice 0, tercer -1 indica que el incremento es negativo meaning se avanza a la izquierda
    if my_list[index] % 2 == 1: #test de numero impar
        deleted=my_list.pop(index)
print(my_list)