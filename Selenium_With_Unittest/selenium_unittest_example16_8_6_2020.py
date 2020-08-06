"""
This page is used to take the screen shot using selenium unittest through a new function defined on the unittest
"""
import time

from selenium import webdriver
import unittest
import os

class UnittestScreenshot(unittest.TestCase):
    """This class tests the screenshots"""

    def setUp(self):
        """This is used to setting up"""
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get('http://demo.guru99.com/insurance/v1/index.php')

    def test_screenshot(self):
        """This is used to test the screen shot"""
        self.driver.find_element_by_id("email").send_keys('sudarshan@yahoo.com')
        self.driver.find_element_by_id('password').send_keys('12343532423')
        self.driver.find_element_by_xpath('//input[@name="submit"]').click()
        self.takescreenshot()
        self.assertTrue(os.path.isfile("E:\\Training_Projects\\Selenium_With_Unittest\\Screenshot2.png"))

    def takescreenshot(self):
        file_location = "E:\\Training_Projects\\Selenium_With_Unittest\\Screenshot2.png"
        self.driver.save_screenshot(file_location)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ =='__main__':
    unittest.main()