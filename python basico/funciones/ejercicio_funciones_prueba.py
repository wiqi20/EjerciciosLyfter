#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#[1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
import math
def is_primo(number):
        if number <=1:
            return False
        if number ==2:
            return True
        if number % 2==0:
            return False
        until_sqrt=int(math.sqrt(number))+1
        for i in range (3,until_sqrt,2):
            if number%i==0:
                return False
        return True


def adding_primo(my_list):
    new_list=[]
    for number in my_list:
        if is_primo(number):
            new_list.append(number)
    return(new_list)


print(adding_primo([1, 4, 6, 7, 13, 9, 67]))