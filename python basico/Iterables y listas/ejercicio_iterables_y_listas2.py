#Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
#Pista: investigue de que otras maneras se puede usar el range.

my_string = "Pizza con piña"
for index in range (len(my_string)):
    print(my_string[-(index+1)])