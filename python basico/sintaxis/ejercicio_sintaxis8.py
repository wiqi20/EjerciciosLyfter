#Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado.
# Luego muestre el resultado de la suma.
count=1
total=0
number=int(input("ingrese un numero "))
while count<=number:
    total=total+count
    count+=1
print(f"el resultado de la sumatoria es {total}")