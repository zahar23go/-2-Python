print("=== ЗАДАНИЕ 2: Високосный год ===")
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
years = [2000, 2024, 1900, 2021]
for y in years:
    print(f"{y}: {'високосный' if is_leap(y) else 'не високосный'}")
