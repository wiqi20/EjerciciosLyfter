import pytest

def divide(number1, number2):
    if number2 == 0:
        raise ValueError("No se puede dividir por cero")
    return number1 / number2
def test_divide_returns_correct_result():
    # Arrange
    number1 = 10
    number2 = 2
    expected_result = 5.0
    # Act
    result = divide(number1, number2)
    # Assert
    assert result == expected_result

def test_divide_by_zero_raises_value_error():
    # Arrange
    number1 = 10
    number2 = 0
    # Act / Assert
    with pytest.raises(ValueError):
        divide(number1, number2)

def test_divide_with_string_raises_type_error():
    # Arrange
    number1 = "10"
    number2 = 2
    # Act / Assert
    with pytest.raises(TypeError):
        divide(number1, number2)