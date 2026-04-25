#Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, 
# seguido del numero ingresado más alto.
my_list=[]
#higher=0
for count in range(0,10):
    number=int(input("ingrese un número "))
    my_list.append(number)
    #if number>higher:
        #higher=number
#print(f"{my_list} -> el número más alto fue {higher}")
print(f"{my_list} -> el número más alto fue {max(my_list)}")