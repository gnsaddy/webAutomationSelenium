import unittest
import time
from selenium import webdriver

timestr = time.strftime("%y%m%d-%H%M%S")


class TestLaunch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            "./chromedriver.exe")  # Store the webdriver in a particular path and call it within the program
        self.driver.get('E:\workspace\webAutomationSelenium\stpAll\loginpage.html')
        self.driver.maximize_window()
        self.driver.save_screenshot("./screenshort/initial-login.png")
        self.driver.save_screenshot("./screenshort/loginScreenBeforeEnteringTheDetails" + timestr + ".png")

    def test_FindClass(self):
        # Valid Uname and Pass
        self.driver.find_element_by_id('User').send_keys('admin')  # Enter User Name
        self.driver.find_element_by_id('Pass').send_keys('root123')  # Enter Password
        self.driver.save_screenshot("./screenshort/logincredentials.png")
        self.driver.save_screenshot("logincredentials" + timestr + ".png")
        self.driver.find_element_by_css_selector('form#frmlog>input:nth-of-type(2)').click()  # clicking login
        self.driver.save_screenshot('./screenshort/success-screen.png')
        self.driver.get("E:\workspace\webAutomationSelenium\stpAll\loginpage.html")
        # invalid username or pass
        self.driver.find_element_by_id('User').send_keys('administrator')  # Enter wrongUser Name
        self.driver.find_element_by_id('Pass').send_keys('root123')  # Enter Password
        self.driver.save_screenshot('./screenshort/wrong-credentials.png')
        self.driver.find_element_by_css_selector('form#frmlog>input:nth-of-type(1)').click()  # clicking reset
        self.driver.save_screenshot('./screenshort/reset.png')
        # Uname empty, password valid
        self.driver.find_element_by_id('User').send_keys('')  # Enter empty Name
        self.driver.find_element_by_id('Pass').send_keys('root123')  # Enter Password
        self.driver.save_screenshot('./screenshort/unameEmpty.png')
        self.driver.find_element_by_css_selector('form#frmlog>input:nth-of-type(1)').click()  # clicking reset
        self.driver.save_screenshot('./screenshort/reset.png')
        # Uname valid, password empty
        self.driver.find_element_by_id('User').send_keys('admin')  # Enter correct Name
        self.driver.find_element_by_id('Pass').send_keys('')  # Enter empty Password
        self.driver.save_screenshot('./screenshort/passEmpty.png')
        self.driver.find_element_by_css_selector('form#frmlog>input:nth-of-type(1)').click()  # clicking reset
        self.driver.save_screenshot('./screenshort/atomationreset.png')
        # Uname & password empty
        self.driver.find_element_by_id('User').send_keys('')  # Enter empty Name
        self.driver.find_element_by_id('Pass').send_keys('')  # Enter empty Password
        self.driver.save_screenshot('./screenshort/bothEmpty.png')
        self.driver.find_element_by_css_selector('form#frmlog>input:nth-of-type(1)').click()  # clicking reset
        self.driver.save_screenshot('./screenshort/reset.png')
        self.assertTrue(self.driver.find_element_by_xpath(".//label"), "Username")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
