from ejercicio_funciones3 import sumatoria

def test_sumatoria_works_with_long_list():
    # Arrange
    numbers = [
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
    expected=sum(numbers)
    # Act
    result = sumatoria(numbers)

    # Assert
    assert result == expected

def test_sumatoria_works_with_ceros():
    # Arrange
    numbers = [0, 0, 0, 0]

    # Act
    result = sumatoria(numbers)

    # Assert
    assert result == 0

def test_sumatoria_works_with_one_number():
    # Arrange
    numbers = [10]

    # Act
    result = sumatoria(numbers)

    # Assert
    assert result == 10