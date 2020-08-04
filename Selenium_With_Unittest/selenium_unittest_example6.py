"""
This is another example of the selenium with which used to test the iframes
"""

from selenium import webdriver
import unittest
import time

class IFrameTest(unittest.TestCase):
    """
    This class is used to test the iframes
    """
    def setUp(self):
        """
        This is used to set up the webpage
        :return: Nothing
        """
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.base_url = 'https://the-internet.herokuapp.com/iframe'

    def test_iframe(self):
        """
        This is used to test the iframes
        :return: Nothing
        """
        self.driver.get(self.base_url)
        self.driver.switch_to.frame(self.driver.find_element_by_id("mce_0_ifr"))
        self.driver.find_element_by_id("tinymce").send_keys("This is new iframe")

    def tearDown(self):
        """
        This is used to close the webpage
        :return: Nothing
        """
        time.sleep(10)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()