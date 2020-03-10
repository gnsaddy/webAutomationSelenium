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
        self.driver.get("https://gnsaddy.github.io/webAutomationSelenium/countWidgets.html")
        radio1 = self.driver.find_elements_by_css_selector('input[name="gender"]')
        radio2 = self.driver.find_elements_by_css_selector('input[name="age"]')
        radio3 = self.driver.find_elements_by_css_selector('input[name="gender"]')
        count = 0

        for i in radio1:
            count += 1
        print("radio button count = ", count)

        for i in radio2:
            count += 1
        print("radio button count = ", count)

        for i in radio3:
            count += 1
        print("radio button count = ", count)
        time.sleep(5)

    # def tearDown(self):
    #     pass


if __name__ == "__main__":
    unittest.main()
