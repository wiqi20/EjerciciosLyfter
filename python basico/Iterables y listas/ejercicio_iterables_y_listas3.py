#Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
my_list = [4, 3, 6, 1, 7]
my_list[0],my_list[-1] = my_list[-1],my_list[0]
print(my_list)