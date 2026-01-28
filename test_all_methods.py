from string_utils import StringUtils

utils = StringUtils()

print("=== Тестирование всех методов StringUtils ===")
print()

test_cases = [
    ("  hello  ", "l"),
    ("SkyPro", "k"),
    ("python", "p"),
    ("", "a"),
    ("123 abc", " "),
]

for text, symbol in test_cases:
    print(f"Текст: {repr(text)}, символ: {repr(symbol)}")
    print(f"  capitalize: {repr(utils.capitalize(text))}")
    print(f"  trim: {repr(utils.trim(text))}")
    print(f"  contains: {utils.contains(text, symbol)}")
    print(f"  delete_symbol: {repr(utils.delete_symbol(text, symbol))}")
    print(f"  reverse_string: {repr(utils.reverse_string(text))}")
    print()
