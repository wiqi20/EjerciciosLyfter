from ejercicio_funciones4 import inverted_string

def test_inverted_string_reverses_word():
    # Arrange
    text = "hello"
    # Act
    result = inverted_string(text)
    # Assert
    assert result == "olleh"

def test_inverted_string_reverses_sentence():
    # Arrange
    text = "hello world"
    # Act
    result = inverted_string(text)
    # Assert
    assert result == "dlrow olleh"

def test_inverted_string_reverses_single_character():
    # Arrange
    text = "a"
    # Act
    result = inverted_string(text)
    # Assert
    assert result == "a"