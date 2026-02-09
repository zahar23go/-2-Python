from selenium import webdriver
from selenium.webdriver.common.by import By

# Просто запускаем Firefox (должен быть установлен)
driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")

# Ждем загрузки
import time
time.sleep(2)

input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("Sky")
time.sleep(1)
input_field.clear()
time.sleep(1)
input_field.send_keys("Pro")

print("Задание 3 выполнено")
driver.quit()