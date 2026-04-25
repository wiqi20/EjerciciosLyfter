#Cree un programa que:
#Pida al usuario su nombre / Si el nombre es numérico (isdigit()), haga raise ValueError("El nombre no puede ser un número")
#Luego pida su edad / Si no es un número válido, capture el ValueError y muestre un mensaje
#Si todo sale bien, imprima un mensaje: "Hola <nombre>, su edad es <edad>"
def name_verify(name:str):
        if name.isdigit():
            raise ValueError("El nombre no puede ser un número")
        return True


def age_verify(age:str):
        if not age.isdigit() or int(age)<=0:
            raise ValueError("su edad debe ser un numero entero positivo")
        return True


def main():
    while True:
        try:
            name=input("Ingrese su nombre: ")
            name_verify(name)
            break
        except ValueError as e:
            print("Error:", e)
    while True:
        try:
            age = input("Ingrese su edad: ")
            age_verify(age)
            break
        except ValueError as e:
            print("Error:", e)
    print(f"Hola {name}, su edad es {int(age)}")
    
main()