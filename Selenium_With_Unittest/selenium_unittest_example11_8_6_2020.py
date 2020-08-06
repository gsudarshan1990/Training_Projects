"""
This is another example of the selenium which is used to take the screen shots with the unittest
"""

from selenium import webdriver
import unittest
import time

class ScreenShotUnittest(unittest.TestCase):
    """
    This class is used to describe how to take the screen shots
    """
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get('http://demo.guru99.com/insurance/v1/index.php')

    def test_screenshot(self):
        """
        This is used to test the screen shot
        :return:
        """
        self.driver.find_element_by_id("email").send_keys("sudarshan@yahoo.com")
        self.driver.find_element_by_id("password").send_keys('12343532423')
        self.driver.find_element_by_xpath("//input[@name='submit']").click()
        destination_screenshot_file = "E:\\Training_Projects\\Selenium_With_Unittest\\Screenshot.png"
        self.driver.get_screenshot_as_file(destination_screenshot_file)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
