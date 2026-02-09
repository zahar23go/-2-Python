# task1.py - РЈСЂРѕРє 5, Р·Р°РґР°РЅРёРµ 1
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
print("РЎС‚СЂР°РЅРёС†Р° Google РѕС‚РєСЂС‹С‚Р°")
driver.quit()
