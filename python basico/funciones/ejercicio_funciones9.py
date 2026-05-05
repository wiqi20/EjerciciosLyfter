#Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras
def counting_letters(my_list, limit):
    new_list=[]
    for i in my_list:  
        if len(i)>limit:
            new_list.append(i)
    return(new_list)


print(counting_letters(['hola', 'mundo', 'python', 'lyfter', 'ejercicio'], 4))
print("This a new print, testing new branch")