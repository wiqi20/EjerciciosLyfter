#Cree un programa que le pida al usuario 
# su nombre, apellido, y edad, y muestre si es un bebé,
# niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

name=input("ingrese su nombre ")
last_name=input("ingrese su apellido ")
age=int(input("ingrese su edad "))

if (age <=2):{
    print("eres un bebé")
}
elif(age<=9):{
    print("eres un niño")
}
elif(age<=12):{
    print("eres un preadolescente")
}
elif(age<=17):{
    print("eres un adolescente")
}
elif(age<=39):{
    print("eres un adulto joven")
}
elif(age<=64):{
    print("eres un adulto")
}
elif(age>=65):{
    print("eres un adulto mayor")
}