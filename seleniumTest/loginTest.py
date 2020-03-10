import os
import unittest
import time

from selenium import webdriver

chromeDriver = "../Drivers/x32/chromedriver.exe"


class ChromeLaunch(unittest.TestCase):

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
        time.sleep(5)
        btn = self.driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/input')

    # def tearDown(self):
    #     pass


if __name__ == "__main__":
    unittest.main()
