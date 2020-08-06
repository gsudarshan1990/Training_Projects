"""
This is an example of multiple tests in the unittest using the selenium
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

class MultipleUnitTest(unittest.TestCase):
    """
    This tests the multiple tests using the unittest case
    """
    def setUp(self):
        """
        This is used for setting up the browser for testing
        :return: Nothing
        """
        self.opts = Options()
        self.opts.headless = True
        self.driver = webdriver.Chrome(options = self.opts,executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")

    def test_title(self):
        """
        This is used to test the title in the browse
        :return: Nothing
        """
        self.driver.get('http://webcode.me')
        self.assertEqual('My html page',self.driver.title)
        print('Title is asserted')

    def test_paragraph(self):
        """
        This is used to test the content in the paragraph
        :return: Nothing
        """
        self.driver.get('http://webcode.me')
        content = self.driver.page_source
        self.assertTrue('Today is a beautiful day' in content)
        print('Content is asserted')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()