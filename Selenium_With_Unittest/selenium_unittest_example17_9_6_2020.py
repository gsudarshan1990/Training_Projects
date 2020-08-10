"""
This is an example of the selenium with unittest which elaborates on the window handles
"""

from selenium import webdriver
import unittest


class WindowHandles(unittest.TestCase):
    """
    This class emphasis on the window handles
    """
    def setUp(self):
        """This is used for setting up the browser"""
        self.driver =  webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://chandanachaitanya.github.io/selenium-practice-site/?languages=Java&enterText=")

    def test_window_handle(self):
        """This is used to test the window handles"""
        parent_handle = self.driver.current_window_handle
        print("Parent Handle ",parent_handle)
        element1 = self.driver.find_element_by_id("win1")
        element1.click()
        handles = self.driver.window_handles
        for handle in handles:
            if(handle != parent_handle):
                self.driver.switch_to.window(handle)
        current_handle = self.driver.current_window_handle
        print(current_handle)

    def tearDown(self):
        """This is used to close the browser"""
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()