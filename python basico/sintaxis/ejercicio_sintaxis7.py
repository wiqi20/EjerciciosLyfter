#Cree un pseudocódigo que le pida un tiempo en segundos al usuario 
# y calcule si es menor o mayor a 10 minutos. Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos.
# Si es mayor, muestre “Mayor”. Si es exactamente igual, muestre “Igual”.
set_time=600
time=int(input("ingrese un tiempo en segundos "))
if time>set_time:
    print("Mayor")
elif time==set_time:
    print("Igual")
elif time<set_time:
    final_time=set_time-time
    print(final_time)