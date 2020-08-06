"""
This page uses the selenium with unittest case to find the size of the window using the execute_script
"""

from selenium import webdriver
import unittest

class WindowSizeUnitTest(unittest.TestCase):
    """
    This class uses the selenium execute_script to find the size of the webpage
    """
    def setUp(self):
        """
        This is used for setup the driver
        :return: Nothing
        """
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")

    def test_size(self):
        self.driver.execute_script('window.location = "http://www.google.com"')
        height = self.driver.execute_script('return window.innerHeight;')
        width = self.driver.execute_script('return window.innerWidth;')
        print('Height:',height)
        print('Width:',width)

    def tearDown(self):
        """
        This is used to quit the driver
        :return: Nothing
        """
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()