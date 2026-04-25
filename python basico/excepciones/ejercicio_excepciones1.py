#Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
#1. Suma
#2. Resta
#3. Multiplicación 
#4. División
#5. Borrar resultado
#Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
#Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.
def suma(actual,num):
    return actual+num


def resta(actual,num):
    return actual-num


def multiplicacion(actual,num):
    return actual*num


def division(actual,num):  
    if num==0:
        print("No se puede dividir por cero")
        return actual # conserva el numero actual a pesar del error al dividir
    return actual/num


def borrar_resultado():
    return 0


def main():
    actual=10
    while True:
        print("\nNúmero actual:", actual)
        print("Que operación desea realizar?")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Borrar resultado")
        print("6. Salir")
        try:
            option=int(input("Seleccione una opción: "))
            if option==1:
                num=float(input("Ingrese el número a sumar: "))
                actual=suma(actual,num)
                print("El resultado es: ", actual)
            elif option==2:
                num=float(input("Ingrese el número a restar: "))
                actual=resta(actual,num)
                print("El resultado es: ", actual)
            elif option==3:
                num=float(input("Ingrese el número a multiplicar: "))
                actual=multiplicacion(actual,num)
                print("El resultado es: ", actual)
            elif option==4:
                num=float(input("Ingrese el número a dividir: "))
                actual=division(actual,num)
                print("El resultado es: ", actual)
            elif option==5:
                actual=borrar_resultado()
                print("El resultado ha sido borrado")
                #option=int(input("Seleccione una opción: "))
            elif option==6:
                print("Saliendo de la calculadora...")
                break
            else:
                print("Seleccione una opción válida")
        except ValueError:
            print("Ingrese un número entero")
main()