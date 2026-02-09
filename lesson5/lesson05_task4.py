from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
time.sleep(2)

# Р—Р°РїРѕР»РЅРµРЅРёРµ С„РѕСЂРјС‹
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)

# РџРѕР»СѓС‡РµРЅРёРµ СЃРѕРѕР±С‰РµРЅРёСЏ
message = driver.find_element(By.ID, "flash").text
print("Р РµР·СѓР»СЊС‚Р°С‚ Р°РІС‚РѕСЂРёР·Р°С†РёРё:", message)

driver.quit()
