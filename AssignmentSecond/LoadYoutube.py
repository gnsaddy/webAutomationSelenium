import time
import unittest

import HtmlTestRunner
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

chromeDriver = "./chromedriver.exe"


class ResumeLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(chromeDriver)
        driver = self.driver
        time.sleep(2)
        driver.maximize_window()

    def test_case_1(self):
        self.driver.get("https://www.devinhouse.codes/pages/login.php")
        try:
            self.driver.execute_script("alert('Testing is progress');")
        except WebDriverException:
            pass
        time.sleep(5)
        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()  # alert closed
        login_email = self.driver.find_element_by_xpath('//*[@id="inputEmail"]')
        login_password = self.driver.find_element_by_xpath('//*[@id="inputPassword"]')
        time.sleep(2)
        try:
            self.driver.execute_script("alert('Sending keys: email and password to input box');")
        except WebDriverException:
            pass
        time.sleep(5)
        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()  # alert closed
        login_email.send_keys('adityaraj.mca18@rvce.edu.in')
        login_password.send_keys('addy123')
        time.sleep(2)
        try:
            self.driver.execute_script("alert('Clicking the submit/login button');")
        except WebDriverException:
            pass
        time.sleep(5)
        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()  # alert closed
        btn_login = self.driver.find_element_by_xpath('//*[@name="loginSubmit"]')
        try:
            self.driver.execute_script("alert('Switching to next page that is user profile');")
        except WebDriverException:
            pass
        time.sleep(5)
        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()  # alert closed
        btn_login.click()
        print("Email and password both correct")
        timeStr = time.strftime("%Y%m%d = %H%M%S")
        # taking screenshots
        self.driver.save_screenshot("./screenShots/" + 'correctLogin_' + timeStr + ".png")
        time.sleep(5)

        # logout and refresh

        self.driver.get('https://www.devinhouse.codes/pages/profile.php')
        try:
            self.driver.execute_script("alert('User profile page');")
        except WebDriverException:
            pass
        time.sleep(5)
        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()  # alert closed
        self.driver.save_screenshot("./screenShots/" + "profile_" + timeStr + ".png")
        try:
            self.driver.execute_script("alert('System trying to logout the user profile');")
        except WebDriverException:
            pass
        time.sleep(5)
        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()  # alert closed
        self.driver.find_element_by_xpath('//*[@id="navcol-1"]/span/a[2]').click()
        time.sleep(5)
        self.driver.refresh()
        self.driver.save_screenshot("./screenShots/" + "home_" + timeStr + ".png")
        try:
            self.driver.execute_script("alert('Again try to login');")
        except WebDriverException:
            pass
        time.sleep(5)
        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()  # alert closed
        self.driver.find_element_by_xpath('//*[@id="navcol-1"]/span/a[1]').click()
        time.sleep(2)
        self.driver.save_screenshot("./screenShots/" + "login_page_" + timeStr + ".png")
        try:
            self.driver.execute_script("alert('Testing login with wrong credentials');")
        except WebDriverException:
            pass
        time.sleep(5)
        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()  # alert closed
        login_email = self.driver.find_element_by_xpath('//*[@id="inputEmail"]')
        login_password = self.driver.find_element_by_xpath('//*[@id="inputPassword"]')
        time.sleep(2)
        login_email.send_keys('wrong_mail@gmail.com')
        login_password.send_keys('addy123')
        # taking screenshots
        self.driver.save_screenshot("./screenShots/" + "wrong_cred_data" + timeStr + ".png")
        time.sleep(2)
        btn_login = self.driver.find_element_by_xpath('//*[@name="loginSubmit"]')
        btn_login.click()
        print("Wrong credentials")
        alertJS = self.driver.switch_to.alert
        print(alertJS.text)
        alertJS.accept()
        # taking screenshots
        self.driver.save_screenshot("./screenShots/" + "wrong_cred_" + timeStr + ".png")
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
