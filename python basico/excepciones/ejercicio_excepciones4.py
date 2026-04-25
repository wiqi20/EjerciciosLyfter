# Cree una función sumar_valores(lista) que:
# Reciba una lista de elementos (strings, enteros, flotantes mezclados)
# Intente convertir cada elemento a tipo float
# Si puede, sume el valor y muestre: "<valor> sumado correctamente"
# Si no puede, muestre: "Elemento inválido: <valor>"
# Al final, imprima la suma total
my_list=[]
def sum_values(my_list):
        total=0
        for i in my_list:
            try:
                number=float(i)
                total+=number
                print(f"{i} sumado correctamente")
            except ValueError:
                print(f"Elemento inválido: {i} ({type(i).__name__})")
        print(f"La suma total es: {total}")
        return total

def list_creation(new_entry):
    my_list.append(new_entry)
    print(f"\nLa lista ingresada es: {my_list}")
    return my_list


def main():
    while True:
        print("\n1. Agregar elemento a la lista")
        print("2. Sumar lista")
        print("3. Salir")
        try:
            option= int(input("\nSeleccione una opción: "))
            if option==1:
                new_entry=input("Ingrese un dato: ")
                list_creation(new_entry)
            elif option==2:
                sum_values(my_list)
                break
            elif option==3:
                print("Saliendo del sistema...")
                break
            else:
                print("\nSeleccione una opcion válida")
        except ValueError:
            print("Debes elegir una opción del menú")


main()