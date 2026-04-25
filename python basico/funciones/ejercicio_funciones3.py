#Cree una función que retorne la suma de todos los números de una lista.
#La función va a tener un parámetro (la lista) y retornar un número (la suma de todos sus elementos).
#[4, 6, 2, 29] → 41
def sumatoria(my_list):
    sum=0
    for number in my_list:
        sum=sum+number
    return(sum)


print(sumatoria([4,6,2,29]))