"""
Exercise 4. Login form
URL: http://the-internet.herokuapp.com/login
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get("http://the-internet.herokuapp.com/login")
    time.sleep(2)

    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")
    time.sleep(1)

    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")
    time.sleep(1)

    login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_btn.click()
    time.sleep(2)

    success_msg = driver.find_element(By.ID, "flash")
    msg_text = success_msg.text
    print("Text from green banner:", msg_text)

    if "You logged into a secure area!" in msg_text:
        print("Login successful!")

    print("Task 4 completed successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()
    print("Browser closed")
