def bubble_sort(list_to_sort):                     # O(1) definición de función
    count_iterations=0                             # O(1) inicialización
    count_interchanges=0                           # O(1) inicialización
    for outer_index in range(0,len(list_to_sort)-1):   # O(n) bucle externo
        has_made_changes = False                   # O(1)
        for index in range(0,len(list_to_sort)-1 -outer_index):  # O(n) bucle interno → total O(n²)
            current_element = list_to_sort[index]  # O(1) acceso a lista
            next_element = list_to_sort[index+1]   # O(1) acceso a lista
            count_iterations+=1                    # O(1) incremento
            if current_element > next_element:     # O(1) comparación
                count_interchanges+=1              # O(1) incremento
                list_to_sort[index] = next_element # O(1) asignación
                list_to_sort[index+1] = current_element # O(1) asignación
                has_made_changes = True            # O(1)
        if not has_made_changes:                   # O(1) verificación
            break                                  # O(1) salida anticipada
    return count_iterations, count_interchanges    # O(1) retorno

my_test_list = [1,2,3,10,4,5,6,7,8]                # O(1) inicialización
iterations, interchanges = bubble_sort(my_test_list) # O(n²) llamada a función
print(f"Lista ordenada: {my_test_list}\nIteraciones:{iterations}\nIntercambios: {interchanges}") # O(1) impresión
