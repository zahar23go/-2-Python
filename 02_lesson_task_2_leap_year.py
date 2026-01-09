def is_year_leap(year):
    return year % 4 == 0


years = [2024, 2023]

for y in years:
    result = is_year_leap(y)
    print(f"год {y}: {result}")
