#Cree un programa que reciba una lista de números y calcule el promedio de los valores,
# luego cree una nueva lista con solo los valores mayores al promedio
my_list=[]
new_list=[]
count=int(input("ingrese la cantidad de números que desea ingresar en la lista: "))
for count in range(0,count):
    number=int(input("ingrese un número "))
    my_list.append(number)
average=sum(my_list)/len(my_list)
for index in range(0,len(my_list)):
    if my_list[index]>average:
        new_list.append(my_list[index])
print(f"Promedio: {average}\nNueva lista: {new_list}")