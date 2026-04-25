#Cree un programa que le pida tres números al usuario y muestre el mayor.
count=0
try:
    greater=int(input("Ingrese un numero: "))
    count += 1
    while count<3:
        number=int(input("ingrese un número "))
        if number>greater:
            greater=number
        count += 1
    print(f"el numero mayor es {greater}")
except ValueError:
    print("ingrese solo números enteros")