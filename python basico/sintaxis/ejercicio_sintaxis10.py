#Cree un diagrama de flujo que pida 3 números al usuario. 
# Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “Correcto”. 
# Sino, mostrar “incorrecto”.
numbers=[]
count=1
search=30
found=bool
while count<=3:
    number=int(input("ingrese un numero "))
    numbers.append(number)
    count+=1
for number in numbers:
    if number==search:
        found=True
if sum(numbers)==30 or found==True:
    print("correcto")
else:
    print("incorrecto")