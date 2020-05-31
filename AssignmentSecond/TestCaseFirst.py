__author__ = 'Aditya'

import unittest

import HtmlTestRunner
from selenium import webdriver
import time

from selenium.common.exceptions import WebDriverException


class TestOpeningGoogle(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver.exe')

    def test_Google(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://www.google.com/')
        try:
            self.driver.execute_script("alert('Opening Google,');")
        except WebDriverException:
            pass
        time.sleep(5)
        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()  # alert closed
        timeStr = time.strftime("%Y%m%d = %H%M%S")
        # taking screenshots
        self.driver.save_screenshot("./screenShots/" + 'google_search' + timeStr + ".png")
        searchBoxPath = driver.find_element_by_xpath("//input[@name='q']")
        # sending request to search in search bar
        try:
            self.driver.execute_script("alert('Searching for RVCE,');")
        except WebDriverException:
            pass
        time.sleep(5)
        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()  # alert closed
        searchBoxPath.send_keys("RVCE")
        time.sleep(3)
        timeStr = time.strftime("%Y%m%d = %H%M%S")
        # taking screenshots
        self.driver.save_screenshot("./screenShots/" + 'page_search' + timeStr + ".png")
        time.sleep(5)
        searchButtom = driver.find_element_by_css_selector("input[type='submit']")
        searchButtom.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
