#Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
#Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.

import random
secret_number=random.randint(1,10)
while True:
    try:
        number= int (input("adivine el numero secreto: "))
        if number==secret_number:
            print(f"adivinaste {number} es el numero secreto!!")
            break
    except ValueError:
        print("ingrese un numero del 1 al 10")