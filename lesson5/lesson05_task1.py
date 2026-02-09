# task1.py - Урок 5, задание 1
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
print("Страница Google открыта")
driver.quit()