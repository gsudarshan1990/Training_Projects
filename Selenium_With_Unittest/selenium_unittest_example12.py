"""
This is an example of selenium with unittest which is used for autocomplete the text box
"""
import time

from selenium import webdriver
import unittest

class UnitTestAutoComplete(unittest.TestCase):
    """
    This class is used for the autocompleting
    """
    def setUp(self):
        """
        This is used for setting up the browser
        :return: Nothing
        """
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("http://www.google.com")

    def  test_autocomplete(self):
        """
        This is used for autocompleteing
        :return: Nothing
        """
        self.driver.find_element_by_name('q').send_keys('selenium')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/ul/li[7]/div/div[2]/div[1]/span').click()
        time.sleep(3)
        self.assertEqual('seleniumhq - Google Search',self.driver.title)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
