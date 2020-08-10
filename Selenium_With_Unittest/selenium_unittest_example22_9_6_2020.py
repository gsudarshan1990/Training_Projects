"""
This is an example of selenium unittest with elobarates mouse hover actions
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
import unittest

class MouseHoverUnitTest(unittest.TestCase):
    """This is used to test the Mouse Hover"""
    def setUp(self):
        """This is used for setting up the browser"""
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get('https://demoqa.com/menu/')

    def test_MouseHoveActions(self):
        """This is used to test the mouse hover action"""
        element1 = self.driver.find_element(By.XPATH,"//a[text()='Main Item 2']")
        try:
            AC(self.driver).move_to_element(element1).perform()
            AC(self.driver).move_to_element(self.driver.find_element(By.XPATH,"//a[text()='SUB SUB LIST »']")).perform()
            AC(self.driver).move_to_element(self.driver.find_element(By.XPATH,"//a[text()='Sub Sub Item 1\\']")).click().perform()
        except:
            print('Mouse Hover Failed')

    def tearDown(self):
        """This is used for closing the browser"""
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()