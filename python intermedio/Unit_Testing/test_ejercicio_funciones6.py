from ejercicio_funciones6 import string_to_list

def test_sorts_multiple_words_alphabetically():
    # Arrange
    text = "python-variable-funcion"
    expected_result = "funcion-python-variable"
    # Act
    result = string_to_list(text)
    # Assert
    assert result == expected_result

def test_returns_same_word_when_only_one_word_is_provided():
    # Arrange
    text = "python"
    expected_result = "python"
    # Act
    result = string_to_list(text)
    # Assert
    assert result == expected_result
    
def test_sorts_words_with_duplicates():
    # Arrange
    text = "python-java-python-c"
    expected_result = "c-java-python-python"
    # Act
    result = string_to_list(text)
    # Assert
    assert result == expected_result