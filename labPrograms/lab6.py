import os
import unittest
import time
from selenium import webdriver

chromeDriver = "../Drivers/x32/chromedriver.exe"
timeStr = time.strftime("%Y%m%d = %H%M%S")
sImage = "webImages"


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(chromeDriver)
        driver = self.driver
        time.sleep(2)
        driver.maximize_window()

    def test_chrome_fn(self):
        self.driver.get("E:\workspace\webAutomationSelenium\labPrograms\src\loginpage.html")
        loginEmail = self.driver.find_element_by_xpath('//*[@id="User"]')
        loginPass = self.driver.find_element_by_xpath('//*[@id="Pass"]')
        time.sleep(2)
        loginEmail.send_keys("admin")
        loginPass.send_keys("admin")
        btn = self.driver.find_element_by_xpath('//*[@id="btn"]')
        # taking screenshots
        self.driver.save_screenshot("../screenShots/loginCred" + timeStr + ".png")
        btn.click()

        time.sleep(5)

        print("Valid both Email and password")
        alertJS = self.driver.switch_to.alert

        print(alertJS.text)
        # self.driver.save_screenshot("../screenShots/prompt" + ".png")
        alertJS.accept()
        # taking screenshots
        self.driver.save_screenshot("../screenShots/" + sImage + timeStr + ".png")

        time.sleep(5)

    def test_chrome_fn1(self):
        self.driver.get("E:\workspace\webAutomationSelenium\labPrograms\src\loginpage.html")
        loginEmail = self.driver.find_element_by_xpath('//*[@id="User"]')
        loginPass = self.driver.find_element_by_xpath('//*[@id="Pass"]')
        time.sleep(2)
        loginEmail.send_keys("amit@gmail.com")
        loginPass.send_keys("testing")
        btn = self.driver.find_element_by_xpath('//*[@id="btn"]')
        btn.click()
        time.sleep(3)
        print("Email not correct and password correct")
        alertJS = self.driver.switch_to.alert
        print(alertJS.text)
        alertJS.accept()
        timeStr = time.strftime("%Y%m%d = %H%M%S")
        sImage = "webImages"
        # taking screenshots
        self.driver.save_screenshot("../screenShots/" + sImage + timeStr + ".png")
        time.sleep(5)

    def test_chrome_fn2(self):
        self.driver.get("E:\workspace\webAutomationSelenium\labPrograms\src\loginpage.html")
        loginEmail = self.driver.find_element_by_xpath('//*[@id="User"]')
        loginPass = self.driver.find_element_by_xpath('//*[@id="Pass"]')
        time.sleep(2)
        loginEmail.send_keys("aditya@gmail.com")
        loginPass.send_keys("wrong")
        btn = self.driver.find_element_by_xpath('//*[@id="btn"]')
        btn.click()
        time.sleep(3)
        print("Email correct and password incorrect")
        alertJS = self.driver.switch_to.alert
        print(alertJS.text)
        alertJS.accept()
        timeStr = time.strftime("%Y%m%d = %H%M%S")
        sImage = "webImages"
        # taking screenshots
        self.driver.save_screenshot("../screenShots/" + sImage + timeStr + ".png")
        time.sleep(5)

    def test_chrome_fn3(self):
        self.driver.get("E:\workspace\webAutomationSelenium\labPrograms\src\loginpage.html")
        loginEmail = self.driver.find_element_by_xpath('//*[@id="User"]')
        loginPass = self.driver.find_element_by_xpath('//*[@id="Pass"]')
        time.sleep(2)
        loginEmail.send_keys("wrong@gmail.com")
        loginPass.send_keys("wrong")
        btn = self.driver.find_element_by_xpath('//*[@id="btn"]')
        btn.click()
        time.sleep(3)
        print("Email and password both incorrect")
        alertJS = self.driver.switch_to.alert
        print(alertJS.text)
        alertJS.accept()
        timeStr = time.strftime("%Y%m%d = %H%M%S")
        sImage = "webImages"
        # taking screenshots
        self.driver.save_screenshot("../screenShots/" + sImage + timeStr + ".png")
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
