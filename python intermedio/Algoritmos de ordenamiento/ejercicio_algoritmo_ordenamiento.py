def bubble_sort(list_to_sort):
    for outer_index in range(len(list_to_sort)-1):
        for index in range(len(list_to_sort)-1,outer_index,-1):
            current_element = list_to_sort[index]
            prev_element = list_to_sort[index-1]
            if current_element < prev_element:
                list_to_sort[index]=prev_element
                list_to_sort[index-1]=current_element
    return list_to_sort

my_list = [9,8,7,6,5,4,3,2,1]
bubble_sort(my_list)
print(my_list)