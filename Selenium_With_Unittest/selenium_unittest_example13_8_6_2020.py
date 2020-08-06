"""
This is another example of the selenium which uses the execute script through the unittest
"""
import time

from selenium import webdriver
import unittest

class JavaScriptExecution(unittest.TestCase):
    """
    This is a sample unittest case which emphasis on the execute_script
    """
    def setUp(self):
        """
        This is used for setting up the browser
        :return: Nothing
        """
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()

    def test_execute_script(self):
        self.driver.execute_script('window.location ="http://www.google.com";')
        element1 = self.driver.execute_script("return document.getElementsByName('q');")
        element1[0].send_keys('yahoo!')

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()