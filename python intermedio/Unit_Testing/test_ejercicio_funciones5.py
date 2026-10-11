from ejercicio_funciones5 import upper_and_lower_cases

def test_counts_uppercase_letters_correctly():
    # Arrange
    expected_upper = 3
    # Act
    upper, lower = upper_and_lower_cases()
    # Assert
    assert upper == expected_upper

def test_counts_lowercase_letters_correctly():
    # Arrange
    expected_lower = 13
    # Act
    upper, lower = upper_and_lower_cases()
    # Assert
    assert lower == expected_lower

def test_returns_correct_upper_and_lower_counts():
    # Arrange
    expected_result = (3, 13)
    # Act
    result = upper_and_lower_cases()
    # Assert
    assert result == expected_result