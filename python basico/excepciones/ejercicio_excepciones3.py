# Cree una función convertir_a_entero(lista) que:
# Reciba una lista de strings
# Intente convertir cada elemento a entero usando int()
# Use try-except para atrapar los errores ValueError
# Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" y continuar con los demás
my_list=[]
def int_convertion(my_list):
        for i in my_list:
            try:
                integer=int(i)
                print(f"{i} ({type(i).__name__}) convertido a {integer} ({type(integer).__name__})")
            except ValueError:
                print(f"No se pudo convertir el elemento: {i} ({type(i).__name__})")


def list_creation(new_entry):
    my_list.append(new_entry)
    print(f"\nLa lista ingresada es: {my_list}")
    return my_list


def main():
    while True:
        print("\n1. Agregar elemento a la lista")
        print("2. Convertir lista a enteros")
        print("3. Salir")
        try:
            option= int(input("\nSeleccione una opción: "))
            if option==1:
                new_entry=input("Ingrese un string: ")
                list_creation(new_entry)
            elif option==2:
                int_convertion(my_list)
                break
            elif option==3:
                print("Saliendo del sistema...")
                break
            else:
                print("\nSeleccione una opcion válida")
        except ValueError:
            print("Debes elegir una opción del menú")


main()