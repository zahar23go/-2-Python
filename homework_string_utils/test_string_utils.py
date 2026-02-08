import pytest
from string_utils import StringUtils

utils = StringUtils()


class TestStringUtils:

    @pytest.mark.parametrize('input_string, expected', [
        # Позитивные проверки:
        ("skypro", "Skypro"),
        ("hello world", "Hello world"),
        ("python", "Python"),

        # Негативные проверки:
        ("", ""),  # пустая строка
        (" ", " "),  # пробел
        ("123abc", "123abc"),  # строка начинается с цифры
    ])
    def test_capitalize(self, input_string, expected):
        """Тестирование функции capitalize"""
        result = utils.capitalize(input_string)
        assert result == expected, f"Ошибка! Вход: '{input_string}', ожидалось: '{expected}', получено: '{result}'"

    @pytest.mark.xfail  # Помечаем как ожидаемо падающий тест
    def test_capitalize_with_special_chars(self):
        """Тестирование capitalize со специальными символами"""
        result = utils.capitalize("!test")
        assert result == "!test", f"Ошибка! Ожидалось '!test', получено '{result}'"

    @pytest.mark.parametrize('input_string, expected', [
        ("   skypro", "skypro"),
        ("  hello", "hello"),
        ("test", "test"),
        ("", ""),
        (" ", ""),
    ])
    def test_trim(self, input_string, expected):
        """Тестирование функции trim"""
        result = utils.trim(input_string)
        assert result == expected

    @pytest.mark.parametrize('string, delimiter, expected', [
        ("a,b,c,d", ",", ["a", "b", "c", "d"]),
        ("1:2:3", ":", ["1", "2", "3"]),
        ("test", ",", ["test"]),
        ("", ",", [""]),
    ])
    def test_to_list(self, string, delimiter, expected):
        """Тестирование функции to_list"""
        result = utils.to_list(string, delimiter)
        assert result == expected

    @pytest.mark.parametrize('string, symbol, expected', [
        ("SkyPro", "S", True),
        ("SkyPro", "k", True),
        ("SkyPro", "U", False),
        ("", "a", False),
    ])
    def test_contains(self, string, symbol, expected):
        """Тестирование функции contains"""
        result = utils.contains(string, symbol)
        assert result == expected

    @pytest.mark.parametrize('string, symbol, expected', [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("Hello World", " ", "HelloWorld"),
        ("test", "x", "test"),
    ])
    def test_delete_symbol(self, string, symbol, expected):
        """Тестирование функции delete_symbol"""
        result = utils.delete_symbol(string, symbol)
        assert result == expected

    @pytest.mark.parametrize('string, symbol, expected', [
        ("SkyPro", "S", True),
        ("SkyPro", "s", False),
        ("", "a", False),
        ("test", "t", True),
    ])
    def test_starts_with(self, string, symbol, expected):
        """Тестирование функции starts_with"""
        result = utils.starts_with(string, symbol)
        assert result == expected

    @pytest.mark.parametrize('string, symbol, expected', [
        ("SkyPro", "o", True),
        ("SkyPro", "O", False),
        ("", "a", False),
        ("test", "t", True),
    ])
    def test_end_with(self, string, symbol, expected):
        """Тестирование функции end_with"""
        result = utils.end_with(string, symbol)
        assert result == expected

    @pytest.mark.parametrize('string, expected', [
        ("", True),
        (" ", True),
        ("SkyPro", False),
        ("  ", True),
    ])
    def test_is_empty(self, string, expected):
        """Тестирование функции is_empty"""
        result = utils.is_empty(string)
        assert result == expected

    @pytest.mark.parametrize('lst, joiner, expected', [
        (["a", "b", "c"], ", ", "a, b, c"),
        (["a", "b", "c"], "-", "a-b-c"),
        ([], ", ", ""),
        (["test"], ", ", "test"),
    ])
    def test_list_to_string(self, lst, joiner, expected):
        """Тестирование функции list_to_string"""
        result = utils.list_to_string(lst, joiner)
        assert result == expected
