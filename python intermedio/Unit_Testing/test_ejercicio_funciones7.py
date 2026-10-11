from ejercicio_funciones7 import adding_primo

def test_returns_only_prime_numbers():
    # Arrange
    numbers = [1, 4, 6, 7, 13, 9, 67]
    expected_result = [7, 13, 67]
    # Act
    result = adding_primo(numbers)
    # Assert
    assert result == expected_result

def test_returns_all_numbers_when_all_are_prime():
    # Arrange
    numbers = [2, 3, 5, 7, 11]
    expected_result = [2, 3, 5, 7, 11]
    # Act
    result = adding_primo(numbers)
    # Assert
    assert result == expected_result
    
def test_returns_empty_list_when_no_primes_exist():
    # Arrange
    numbers = [1, 4, 6, 8, 9, 10]
    expected_result = []
    # Act
    result = adding_primo(numbers)
    # Assert
    assert result == expected_result