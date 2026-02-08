from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

button = driver.find_element(
    By.XPATH,
    "//button[text()='Button with Dynamic ID']"
)
button.click()

driver.quit()
