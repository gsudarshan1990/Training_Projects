"""
This is example of the selenium with unittest using the ActionChains example
"""

from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains as AC
import time

class MouseActions(unittest.TestCase):
    """
    This class is used to explain the action chains
    """
    def setUp(self):
        """
        This is used to setting up the browser
        :return: Nothing
        """
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.base_url = 'https://jqueryui.com/droppable/'

    def test_mouse_actions(self):
        """
        This is used to test the mouse actions
        :return: Nothing
        """
        self.driver.get(self.base_url)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@src='/resources/demos/droppable/default.html']"))
        drag_element = self.driver.find_element_by_id("draggable")
        drop_element = self.driver.find_element_by_id("droppable")
        AC(self.driver).drag_and_drop(drag_element,drop_element).perform()
        time.sleep(3)

    def tearDown(self):
        """
        This is used to close the browser
        :return: Nothing
        """
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()