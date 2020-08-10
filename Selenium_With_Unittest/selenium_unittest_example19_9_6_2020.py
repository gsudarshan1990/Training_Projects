"""
This is an example of selenium with unittest which further elaborates on the window handle
"""
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class WindowSwitchUnitTest(unittest.TestCase):
    """This class is used for windows handles"""
    def setUp(self):
        """This is used for setting up the browser"""
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://chandanachaitanya.github.io/selenium-practice-site/?languages=Java&enterText=")

    def test_window_switch(self):
        """This is used for switching the windows"""
        parent_handle = self.driver.current_window_handle
        print('Parent Handle', parent_handle)
        element1 = self.driver.find_element_by_id("win2")
        element1.click()
        handles = self.driver.window_handles
        for handle in handles:
            if (handle!=parent_handle):
                self.driver.switch_to.window(handle)
                self.driver.maximize_window()
                self.driver.find_element_by_name("q").send_keys("selenium")
                self.driver.find_element_by_name("q").send_keys(Keys.ENTER)

        self.driver.switch_to.window(parent_handle)
        time.sleep(3)
        print(self.driver.title)

    def tearDown(self):
        """This is used close the browser"""
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()