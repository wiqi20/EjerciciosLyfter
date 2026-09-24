def manual_add(n):
    result = 0
    for i in range(1, n + 1):   # O(n) recorrido
        result += i             # O(1) suma
    return result               # O(1) retorno


def add_formula(n):
    return n * (n + 1) // 2     # O(1) operación constante
#¿Cuál es la complejidad de cada versión?
#manual_add O(n), porque recorre todos los números hasta n
#add_fomula O(1)
#¿Qué versión usaría si number = 1 000 000 000? ¿Por qué?
#Usaría la versión con fórmula (O(1)), porque escala mucho mejor y 
# evita recorrer un número enorme de iteraciones.


def linear_search(my_list, target):
    for item in my_list:              # O(n) recorrido completo
        if item == target:            # O(1) comparación
            return True               # O(1) retorno inmediato
    return False                      # O(1) retorno final

def binary_search(my_list, target):
    low = 0                           # O(1)
    high = len(my_list) - 1           # O(1)
    while low <= high:                # O(log n) reducción del rango
        mid = (low + high) // 2       # O(1)
        if my_list[mid] == target:    # O(1)
            return True               # O(1)
        elif my_list[mid] < target:   # O(1)
            low = mid + 1             # O(1)
        else:
            high = mid - 1            # O(1)
    return False                      # O(1)

#Preguntas:
#¿Cuál es la complejidad de cada algoritmo?
#
#O(log n)
#Binary search
#¿En qué condiciones conviene usar cada uno?
#Linear search:
#Conviene cuando la lista es pequeña o no está ordenada.
#No requiere preprocesamiento.
#Binary search:
#Conviene cuando la lista es grande y está ordenada.
#Mucho más eficiente en listas largas.

#¿Qué pasa si la lista no está ordenada?
#Linear search funciona sin problema, porque recorre secuencialmente.
#Binary search deja de ser válido: si la lista no está ordenada, 
# el algoritmo puede dar resultados incorrectos, ya que depende de la propiedad
#  de orden para descartar mitades.


def print_all_pairs(my_dict):                     # O(1) definición de función
    for key1 in my_dict:                          # O(n) recorrido de claves
        for key2 in my_dict:                      # O(n) recorrido de claves → total O(n²)
            print(f"{key1}-{key2}")               # O(1) operación constante

#¿Cuál es la complejidad temporal?
#O(n²)
#A¿Cuanto dura si hay 1 millón de claves?
#Si el diccionario tiene 1,000,000 claves, el algoritmo intentará imprimir un trillon de impresiones 