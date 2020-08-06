"""
This is an example of the selenium along with the unittest which uses the execute_script for finding the screw
"""
import time

from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By

class TestScrollUnittest(unittest.TestCase):
    """
    This class is used to test the scrolling
    """
    def setUp(self):
        """
        This is used for setting up the browser
        :return: Nothing
        """
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get('https://www.w3schools.com/jsref/met_document_getelementbyid.asp')

    def test_scroll_up(self):
        """ This is used to scroll down"""
        self.driver.execute_script('window.scrollBy(0,-1000);')
        time.sleep(3)

    def test_scroll_down(self):
        """This is used to scroll up"""
        self.driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(3)

    def test_scroll_into_view(self):
        """This is used to scroll into view"""
        element1 = self.driver.find_element(By.XPATH,"//a[text()='Try it Yourself »']")
        self.driver.execute_script('arguments[0].scrollIntoView(true);',element1)
        time.sleep(2)
        self.driver.execute_script('window.scrollBy(0,-150);')

    def tearDown(self):
        """
        This is used to quit the browser
        :return: Nothing
        """
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()