def validated_bubble_sort(list_to_sort):
    if not list_to_sort:
        raise ValueError("La lista esta vacia")
    if not all(isinstance(x,(int,float))for x in list_to_sort):
        raise TypeError("La lista contiene elementos no numericos")
    count_iterations=0
    count_interchanges=0
    for outer_index in range(0,len(list_to_sort)-1):
        has_made_changes = False
        for index in range(0,len(list_to_sort)-1 -outer_index):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index+1]
            count_iterations+=1
            if current_element > next_element:
                count_interchanges+=1
                list_to_sort[index] = next_element
                list_to_sort[index+1] = current_element
                has_made_changes = True
        if not has_made_changes:
            break
    return list_to_sort, count_iterations, count_interchanges

try:
    my_test_list = [1,2,3,10,"YES",5,6,7,8]
    result, iterations, interchanges = validated_bubble_sort(my_test_list)
    print(f"Lista ordenada: {result}\nIteraciones:{iterations}\nIntercambios: {interchanges}")
except Exception as e:
    print("Error:", e)