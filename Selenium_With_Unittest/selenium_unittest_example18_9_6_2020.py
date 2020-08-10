"""
This is an example of the selenium unittest which elaborates the window switch however not to new tab
"""

from selenium import webdriver
import unittest

class SwitchWindowUnittest(unittest.TestCase):
    """This is used to switch to the new window"""
    def setUp(self):
        """This is used for setting up the browser"""
        self.driver = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://chandanachaitanya.github.io/selenium-practice-site/?languages=Java&enterText=")

    def test_switch_window(self):
        """This is used for testing the window"""
        parent_handle = self.driver.current_window_handle
        print('Parent Handle',parent_handle)
        element2 = self.driver.find_element_by_id("win2")
        element2.click()
        handles = self.driver.window_handles
        for handle in handles:
            if(handle != parent_handle):
                self.driver.switch_to.window(handle)
                self.driver.maximize_window()
                print(self.driver.title)


    def tearDown(self):
        """This is used to close the browser"""
        self.driver.quit()

if __name__ =='__main__':
    unittest.main()