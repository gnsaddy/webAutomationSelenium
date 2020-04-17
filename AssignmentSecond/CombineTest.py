import os
import time
import unittest

import HtmlTestRunner
from selenium import webdriver

direct = os.getcwd()


class Search(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('../Drivers/x32/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_open_google(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_xpath("//input[@role='combobox']").send_keys("Selenium Web Automation")
        time.sleep(3)
        self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
            output='E:/workspace/webAutomationSelenium/AssignmentSecond/reports')))
