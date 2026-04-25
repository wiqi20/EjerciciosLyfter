#Cree un programa que cuente cuántas veces aparece un número específico en una lista. 
# Pida al usuario una lista de números y otro número a buscar
my_list=[]
count_search=0
try:
    count=int(input("ingrese la cantidad de números que desea ingresar en la lista: "))
    for count in range(0,count):
        number=int(input("ingrese un número: "))
        my_list.append(number)
    number_search=int (input("ingrese el número que desea buscar: "))
    for index in range(0,len(my_list)):
        if number_search==my_list[index]:
            count_search+=1
    print(f"el número {number_search} aparece {count_search} veces en la lista")
except ValueError:
    print("ingrese un número válido")