#Cree un diagrama de flujo que tenga un numero secreto del 1 al 10, y le pida al usuario adivinar ese número. 
# El algoritmo no debe terminar hasta que el usuario adivine el numero.
secret_number=2
while True:
    try:
        number= int (input("adivine el numero secreto: "))
        if number==secret_number:
            print(f"adivinaste {number} es el numero secreto!!")
            break
    except ValueError:
        print("ingrese un numero del 1 al 10")