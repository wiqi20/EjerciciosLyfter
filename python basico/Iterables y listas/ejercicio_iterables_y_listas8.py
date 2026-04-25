#Cree un programa que muestre el valor más pequeño de una lista sin usar min().
#Use una variable para comparar uno a uno
my_list=[]
count=int(input("ingrese la cantidad de números que desea ingresar en la lista: "))
for count in range(0,count):
    number=int(input("ingrese un número "))
    my_list.append(number)
lower=my_list[0]
for index in my_list[1:]:
    if index<lower:
        lower=index
print(f"el número más bajo fue {lower}")