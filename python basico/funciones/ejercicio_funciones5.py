#Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.
def upper_and_lower_cases():
    mystring="I love Nación Sushi"
    upper=0
    lower=0
    for index in mystring:
        if index.isupper():
            upper+=1
        elif index.islower():
            lower+=1
    print(f"There’s {upper} upper cases and {lower} lower cases")


upper_and_lower_cases()