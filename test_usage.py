from string_utils import StringUtils

def main():
    utils = StringUtils()
    
    # Тестируем методы
    print('1. capitalize:', utils.capitalize('hello world'))
    print('2. trim:', utils.trim('   hello   '))
    print('3. contains:', utils.contains('hello', 'ell'))
    print('4. contains (false):', utils.contains('hello', 'xyz'))
    print('5. delete_symbol:', utils.delete_symbol('hello world', 'o'))
    print('6. delete_symbol (нет символа):', utils.delete_symbol('hello', 'x'))

if __name__ == '__main__':
    main()
