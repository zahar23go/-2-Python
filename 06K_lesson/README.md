# Создаём README.md в чистом UTF-8 без BOM
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
$readmeContent = @"
# Домашнее задание к уроку 6K
## Автотесты на Selenium WebDriver

### 📋 Структура проекта
- `test_01_form.py` - тест проверки формы с валидацией полей (браузер Edge)
- `test_02_calc.py` - тест калькулятора с задержкой 45 секунд (браузер Chrome)
- `test_03_shop.py` - тест интернет-магазина SauceDemo (браузер Firefox)
- `requirements.txt` - зависимости проекта
- `.gitignore` - список игнорируемых файлов
- `README.md` - описание проекта

### 🚀 Запуск тестов
```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск всех тестов
python -m pytest -v

# Запуск конкретного теста
python -m pytest test_01_form.py -v
python -m pytest test_02_calc.py -v
python -m pytest test_03_shop.py -v