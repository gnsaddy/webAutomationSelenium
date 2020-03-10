from selenium import webdriver
import time

driver = webdriver.Chrome('../Drivers/x32/chromedriver.exe')

driver.get("https://gnsaddy.github.io/webAutomationSelenium/")
loginEmail = driver.find_element_by_xpath('//*[@id="inputEmail"]')
loginPass = driver.find_element_by_xpath('//*[@id="inputPassword"]')
time.sleep(2)
loginEmail.send_keys("aditya@gmail.com")
loginPass.send_keys("testing")
time.sleep(5)
btn = driver.find_element_by_xpath('//*[@id="btnLogin"]')
btn.click()
