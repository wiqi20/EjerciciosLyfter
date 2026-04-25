#Cree un programa que verifique si todos los elementos de una lista son positivos
my_list = [3, 6, 0, -2, 4]
count=0
for index in range(0,len(my_list)):
    if my_list[index]<=0:
        count+=1
if count>0:
    print(f"en la lista hay al menos {count} elementos negativo o cero")
else:
    print("todos los elementos son positivos")