from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
time.sleep(2)

# Заполнение формы
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)

# Получение сообщения
message = driver.find_element(By.ID, "flash").text
print("Результат авторизации:", message)

driver.quit()
