"""
This is an example of selenium with unitest which elaborates on the mousehover slider
"""
import time

from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC

class SliderUnittest(unittest.TestCase):
    """This class is used to test the slider"""
    def setUp(self):
        """This is used to setup the browser for testing purpose"""
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get('https://jqueryui.com/slider/')

    def test_slider(self):
        """This is used to test the slider"""
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME,"demo-frame"))
        element1 = self.driver.find_element(By.ID,"slider")
        try:
            AC(self.driver).drag_and_drop_by_offset(element1,100,0).perform()
            time.sleep(2)
            filename ='E:\\Training_Projects\\Selenium_With_Unittest\\Slider.png'
            self.driver.save_screenshot(filename)
        except NotADirectoryError:
            print('Could not Drag')

    def tearDown(self):
        """This is used to close the browser"""
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
