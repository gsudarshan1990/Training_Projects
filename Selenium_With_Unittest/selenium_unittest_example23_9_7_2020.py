"""
This is an example of selenium with unittest along with mouse hover actions which are related to drag and drop
"""
import time

from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC

class DragDropUnittest(unittest.TestCase):
    """This class implements drag and drop case via selenium unittest"""
    def setUp(self):
        """This is used set up the browser for automation"""
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get('https://demoqa.com/droppable/')

    def test_Drag_Drop(self):
        """This is used to test the drag and drop"""
        AC(self.driver).drag_and_drop(self.driver.find_element(By.ID,"draggable"),self.driver.find_element(By.ID,'droppable')).perform()
        time.sleep(1)
        filename = "E:\\Training_Projects\\Selenium_With_Unittest\\drag_drop.png"
        try:
            self.driver.save_screenshot(filename)
        except NotADirectoryError:
            print('Could not Take the Screen Shot')

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()