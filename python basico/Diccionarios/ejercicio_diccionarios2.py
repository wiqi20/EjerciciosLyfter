#Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
#Ejemplos:
#list_a = [’first_name’, ‘last_name’, ‘role’]
#list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]
#→ {’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}
my_dictionary={}
list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]
for index in range(0,len(list_a)):
    my_dictionary[list_a[index]]=list_b[index]
print(my_dictionary)