from selenium import webdriver
import unittest
import time


class CountWidget(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../Drivers/x32/chromedriver.exe")
        driver = self.driver
        time.sleep(2)
        driver.maximize_window()

    def test_chrome_fn(self):
        self.driver.get("https://gnsaddy.github.io/webAutomationSelenium/countWidgets.html")
        radio1 = self.driver.find_elements_by_css_selector('input[name="gender"]')
        radio2 = self.driver.find_elements_by_css_selector('input[name="age"]')
        radio3 = self.driver.find_elements_by_css_selector('input[name="gender"]')
        count = 0

        for i in radio1 and radio2 and radio3:
            count += 1
        print("radio button count = ", count)
        time.sleep(5)

    # def tearDown(self):
    #     pass


if __name__ == "__main__":
    unittest.main()

