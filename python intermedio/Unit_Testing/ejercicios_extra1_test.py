def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def average(numbers):
    return sum(numbers) / len(numbers)

def test_add_with_positive_numbers():
    # Arrange
    num1 = 10
    num2 = 5
    expected_result = 15
    # Act
    result = add(num1, num2)
    # Assert
    assert result == expected_result

def test_subtract_with_negative_numbers():
    # Arrange
    num1 = -10
    num2 = -5
    expected_result = -5
    # Act
    result = subtract(num1, num2)
    # Assert
    assert result == expected_result

def test_average_with_zeros():
    # Arrange
    numbers = [0, 0, 0]
    expected_result = 0
    # Act
    result = average(numbers)
    # Assert
    assert result == expected_result