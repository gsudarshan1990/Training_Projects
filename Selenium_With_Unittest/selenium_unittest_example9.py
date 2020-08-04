"""
This is example of selenium with unittest and assertions
"""

from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys



class SeleniumAssertionUnittest(unittest.TestCase):
    """
    This is the class which tests the selenium unittests using the assertions
    """
    def setUp(self):
        """
        This is used to setup the browser test
        :return: Nothing
        """
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.base_url = "https://www.google.com/"

    def test_unittestassertions(self):
        """
        This is used to test the assertions
        :return: Nothing
        """
        self.driver.get(self.base_url)
        self.driver.find_element_by_name('q').send_keys('Selenium')
        self.driver.find_element_by_name('q').send_keys(Keys.ENTER)
        self.assertEqual(self.driver.title,'Selenium - Google Search')
        lists = self.driver.find_elements_by_class_name("r")
        total_search = len(lists)
        print
        self.assertEqual(total_search,12)
        print('All Asserts are passed')

    def tearDown(self):
        """
        This is used to close the test
        :return: Nothing
        """
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()