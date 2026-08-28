def bubble_sort(list_to_sort):
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
    return count_iterations, count_interchanges

my_test_list = [1,2,3,10,4,5,6,7,8]
iterations, interchanges = bubble_sort(my_test_list)
print(f"Lista ordenada: {my_test_list}\nIteraciones:{iterations}\nIntercambios: {interchanges}")