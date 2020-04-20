__author__ = 'Aditya'

import unittest

import HtmlTestRunner
from selenium import webdriver
import time


class TestOpeningGoogle(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../Drivers/x32/chromedriver.exe')

    def test_Google(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('http://google.com')
        searchBoxPath = driver.find_element_by_xpath("//input[@role='combobox']")
        # sending request to search in search bar
        searchBoxPath.send_keys("RVCE")
        time.sleep(3)
        searchButtom = driver.find_element_by_css_selector("input[type='submit']")
        searchButtom.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
