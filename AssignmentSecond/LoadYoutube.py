__author__ = 'Aditya'

import unittest

import HtmlTestRunner
from selenium import webdriver
import time


class LaunchFacebook(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('../Drivers/x32/chromedriver.exe')

    def test_FacebookTest(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://www.facebook.com/')

        time.sleep(1)
        email = driver.find_element_by_id("email")
        password = driver.find_element_by_id("pass")  # ("pass")

        loginBtn = driver.find_element_by_css_selector("input[type='submit']")
        email.send_keys('fakeuser123@gmail.com')
        password.send_keys(str('fakepassword'))
        loginBtn.click()

    def test_FacebookTest_correct(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://www.facebook.com/')

        time.sleep(1)
        email = driver.find_element_by_id("email")
        password = driver.find_element_by_id("pas")  # ("pass")

        loginBtn = driver.find_element_by_css_selector("input[type='submit']")
        email.send_keys('fakeuser123@gmail.com')
        password.send_keys(str('fakepassword'))
        loginBtn.click()


if __name__ == '__main__':
    unittest.main()
#
# if __name__ == '__main__':
#     unittest.main(
#         unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
#             output='E:/workspace/webAutomationSelenium/AssignmentSecond/reports')))
