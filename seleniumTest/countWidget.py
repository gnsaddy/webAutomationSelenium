import time
import unittest
from selenium.webdriver.support.ui import Select
from selenium import webdriver

chromeDriver = "../Drivers/x32/chromedriver.exe"


class countWidget(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(chromeDriver)
        driver = self.driver
        # time.sleep(2)
        driver.maximize_window()

    def test_count1(self):
        self.driver.get("https://gnsaddy.github.io/webAutomationSelenium/countWidgets.html")
        radio1 = self.driver.find_elements_by_css_selector('input[name="gender"]')
        radio2 = self.driver.find_elements_by_css_selector('input[name="age"]')
        radio3 = self.driver.find_elements_by_css_selector('input[name="gender"]')
        count = 0

        for i in radio1:
            count += 1
        print("\nradio button count = ", count)

        for i in radio2:
            count += 1
        print("\nradio button count = ", count)

        for i in radio3:
            count += 1
        print("\nradio button count = ", count)
        print("----------------------------------------------------------")
        time.sleep(5)

    def test_count2(self):
        self.driver.get("https://gnsaddy.github.io/webAutomationSelenium/countWidgets.html")
        textBox = self.driver.find_elements_by_css_selector('input[type="text"]')
        count = 0
        count1 = 0

        for i in textBox:
            count += 1
        print("\ntext box count = ", count)
        print("----------------------------------------------------------")
        time.sleep(5)

    def test_count3(self):
        self.driver.get("https://gnsaddy.github.io/webAutomationSelenium/countWidgets.html")
        con = 0
        dropdown = Select(self.driver.find_element_by_xpath("//*[@id='cars']"))
        con += 1
        dropdown2 = Select(self.driver.find_element_by_xpath('//*[@id="bikes"]'))
        con += 1

        print("\nCombobox count : ", con)

        count = 0

        for i in dropdown.options:
            count += 1
        print("\ncombobox value count = ", count)
        val = []
        for element in dropdown.options:
            val.append([element.get_attribute("value")])
            print(element.get_attribute("value"))
        print("\ncombobox value count =  ", len(val))
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
