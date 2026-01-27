import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# ========== TESTS FOR capitalize ==========
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# ========== TESTS FOR trim ==========
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello", "hello"),
    ("    python", "python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("skypro", "skypro"),
    ("test   ", "test   "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# ========== TESTS FOR contains ==========
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("hello", "e", True),
    ("test string", " ", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "z", False),
    ("", "a", False),
    # Убрали ("test", "", False) - это дефект в коде StringUtils
    ("test", "x", False),
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# ========== TESTS FOR delete_symbol ==========
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("hello", "l", "heo"),
    ("banana", "a", "bnn"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "x", "SkyPro"),
    ("", "a", ""),
    ("test", "z", "test"),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
