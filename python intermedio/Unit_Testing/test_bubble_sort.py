import pytest
from bubble_sort import bubble_sort


def test_buble_sort_works_with_small_list():
    #Arange
    list_to_sort=[2,1,4]
    #Act
    bubble_sort(list_to_sort)
    #Assert
    assert list_to_sort == [1,2,4]

def test_buble_sort_works_with_big_list():
    #Arange
    list_to_sort=[
    87, 12, 453, 29, 178, 65, 901, 34, 721, 15,
    88, 509, 233, 67, 14, 390, 812, 55, 301, 99,
    420, 186, 732, 41, 560, 25, 973, 108, 357, 689,
    22, 814, 470, 156, 83, 291, 643, 17, 928, 376,
    51, 701, 240, 95, 614, 38, 857, 483, 129, 764,
    20, 598, 311, 46, 982, 175, 632, 89, 415, 708,
    13, 840, 267, 58, 924, 302, 147, 676, 31, 555,
    199, 783, 62, 914, 350, 27, 605, 442, 119, 860,
    75, 518, 283, 11, 947, 366, 52, 690, 248, 803,
    140, 599, 74, 921, 157, 435, 286, 18, 772, 504,
    91, 663, 329, 49, 885, 213, 730, 126, 571, 398,
    66, 947, 182, 624, 44, 785, 270, 936, 103, 511
]
    expected=sorted(list_to_sort)
    #Act
    bubble_sort(list_to_sort)
    #Assert
    assert list_to_sort == expected

def test_buble_sort_works_with_empty_list():
    #Arange
    list_to_sort=[]
    #Act
    bubble_sort(list_to_sort)
    #Assert
    assert list_to_sort == []
def test_bubble_sort_raises_error_when_parameter_is_not_a_list():
    # Arrange
    not_a_list = "hola"

    # Act / Assert
    with pytest.raises(TypeError):
        bubble_sort(not_a_list)

def test_bubble_sort_works_with_duplicates():
    data = [3, 1, 3, 2]
    bubble_sort(data)
    assert data == [1, 2, 3, 3]

def test_bubble_sort_works_with_negative_numbers():
    data = [5, -1, 3, -7]
    bubble_sort(data)
    assert data == [-7, -1, 3, 5]

def test_bubble_sort_works_with_one_element():
    data = [5]
    bubble_sort(data)
    assert data == [5]