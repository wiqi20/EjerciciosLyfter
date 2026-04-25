#Pida al usuario un número del 1 al 10
#Muestre su tabla de multiplicar del 1 al 12
count=1
num=int(input("ingrese un número del 1 al 10 "))
while count<=12:
    product=num*count
    print(f"{num}x{count}= {product}")
    count+=1