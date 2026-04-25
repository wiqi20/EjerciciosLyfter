#Convertidor de unidades de temperatura
#Pida al usuario ingresar una temperatura en Celsius
#Conviértala a Fahrenheit y Kelvin
#Muestre los tres valores
celsius=int(input("ingrese una temperatura en grados celsius "))
fahrenheit=(celsius*9/5)+32
kelvin=celsius+273.15
print(f"{celsius} °C equivalen a {fahrenheit} °F y {kelvin} K")