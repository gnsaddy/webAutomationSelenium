from selenium import webdriver
import os

driver = webdriver.Chrome("../Drivers/x32/chromedriver.exe")
driver.get("http://localhost:63342/webAutomationSelenium/countWidgets.html")

radio = driver.find_elements_by_css_selector('input[name="gender]')
count = 0

for i in radio:
    count += 1

print("radio button count = ", count)
driver.quit()
