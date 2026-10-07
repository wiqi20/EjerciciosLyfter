def print_numbers_times_2(numbers_list):        # O(1) definición de función
    for number in numbers_list:                 # O(n) recorrido de la lista
        print(number * 2)                       # O(1) operación constante

def check_if_lists_have_an_equal(list_a, list_b):     # O(1) definición de función
    for element_a in list_a:                          # O(n) recorrido de list_a
        for element_b in list_b:                      # O(n) recorrido de list_b → total O(n²)
            if element_a == element_b:                # O(1) comparación
                return True                           # O(1) retorno inmediato
                
    return False                                      # O(1) retorno final

def print_10_or_less_elements(list_to_print):     # O(1) definición de función
    list_len = len(list_to_print)                 # O(1) obtener longitud de la lista
    for index in range(min(list_len, 10)):        # O(n) recorrido, pero acotado a 10 → O(1)
        print(list_to_print[index])               # O(1) acceso e impresión

def generate_list_trios(list_a, list_b, list_c):      # O(1) definición de función
    result_list = []                                  # O(1) inicialización
    for element_a in list_a:                          # O(n) recorrido de list_a
        for element_b in list_b:                      # O(n) recorrido de list_b
            for element_c in list_c:                  # O(n) recorrido de list_c → total O(n³)
                result_list.append(f'{element_a} {element_b} {element_c}')  # O(1) operación constante
                
    return result_list                                # O(1) retorno
