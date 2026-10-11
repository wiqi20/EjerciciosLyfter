from unittest.mock import mock_open, patch
import pytest

def read_lines(path):
    with open(path, 'r') as f:
        return f.readlines()

def test_read_lines_returns_expected_lines():
    # Arrange
    mock_file_content = "line1\nline2\nline3\n"
    expected_result = ["line1\n", "line2\n", "line3\n"]
    # Act
    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        result = read_lines("fake_file.txt")
    # Assert
    assert result == expected_result

def test_read_lines_opens_file_with_correct_parameters():
    # Arrange
    mocked_open = mock_open(read_data="hello\n")
    # Act
    with patch("builtins.open", mocked_open):
        read_lines("fake_file.txt")
    # Assert
    mocked_open.assert_called_once_with("fake_file.txt", "r")

def test_read_lines_raises_file_not_found_error():
    # Arrange
    path = "missing_file.txt"
    # Act / Assert
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            read_lines(path)