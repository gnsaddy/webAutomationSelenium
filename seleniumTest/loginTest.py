import os
import unittest
import time
from selenium import webdriver

chromeDriver = "../Drivers/x32/chromedriver.exe"


class COuntWidget(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(chromeDriver)
        driver = self.driver
        time.sleep(2)
        driver.maximize_window()

    def test_chrome_fn(self):
        self.driver.get("https://gnsaddy.github.io/webAutomationSelenium/")
        loginEmail = self.driver.find_element_by_xpath('//*[@id="inputEmail"]')
        loginPass = self.driver.find_element_by_xpath('//*[@id="inputPassword"]')
        time.sleep(2)
        loginEmail.send_keys("aditya@gmail.com")
        loginPass.send_keys("testing")
        btn = self.driver.find_element_by_xpath('//*[@id="btnLogin"]')
        btn.click()
        print("Valid both Email and password")
        loginEmail.clear()
        loginPass.clear()
        time.sleep(5)

    def test_chrome_fn1(self):
        self.driver.get("https://gnsaddy.github.io/webAutomationSelenium/")
        loginEmail = self.driver.find_element_by_xpath('//*[@id="inputEmail"]')
        loginPass = self.driver.find_element_by_xpath('//*[@id="inputPassword"]')
        time.sleep(2)
        loginEmail.send_keys("amit@gmail.com")
        loginPass.send_keys("testing")
        btn = self.driver.find_element_by_xpath('//*[@id="btnLogin"]')
        btn.click()
        print("Email not correct and password correct")
        loginEmail.clear()
        loginPass.clear()
        time.sleep(5)

    def test_chrome_fn2(self):
        self.driver.get("https://gnsaddy.github.io/webAutomationSelenium/")
        loginEmail = self.driver.find_element_by_xpath('//*[@id="inputEmail"]')
        loginPass = self.driver.find_element_by_xpath('//*[@id="inputPassword"]')
        time.sleep(2)
        loginEmail.send_keys("aditya@gmail.com")
        loginPass.send_keys("wrong")
        btn = self.driver.find_element_by_xpath('//*[@id="btnLogin"]')
        btn.click()
        print("Email correct and password incorrect")
        loginEmail.clear()
        loginPass.clear()
        time.sleep(5)

    def test_chrome_fn3(self):
        self.driver.get("https://gnsaddy.github.io/webAutomationSelenium/")
        loginEmail = self.driver.find_element_by_xpath('//*[@id="inputEmail"]')
        loginPass = self.driver.find_element_by_xpath('//*[@id="inputPassword"]')
        time.sleep(2)
        loginEmail.send_keys("wrong@gmail.com")
        loginPass.send_keys("wrong")
        btn = self.driver.find_element_by_xpath('//*[@id="btnLogin"]')
        btn.click()
        print("Email and password both incorrect")
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
