#Cree un programa que le pida al usuario ingresar 5 palabras. 
# Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras
my_list=[]
new_list=[]
count=4
for index in range(0,5):
    word=str(input("ingrese una palabra "))
    my_list.append(word)
    if len(word)>4:
        new_list.append(word)
print(f"mi lista: {my_list}\nNueva lista: {new_list}")