"""
This is another example of the selenium with the unittest which uses the alerts
"""

from selenium import webdriver
import unittest
from selenium.webdriver.common.alert import Alert
import time

class AlertTest(unittest.TestCase):
    """
    This class is used to perfrom the unittest alerts
    """
    def setUp(self):
        """
        This is used to setup the driver
        :return: Nothing
        """
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.base_url = "http://testautomationpractice.blogspot.com/"

    def test_alerts(self):
        """
        This is used to test the alerts
        :return: Nothing
        """
        self.driver.get(self.base_url)
        self.driver.find_element_by_xpath("//button[text()='Click Me']").click()
        Alert(self.driver).accept()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[text()='Click Me']").click()
        Alert(self.driver).dismiss()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[text()='Click Me']").click()
        print(Alert(self.driver).text)

    def tearDown(self):
        """
        This is used to close the browser
        :return:
        """
        time.sleep(5)
        self.driver.quit()

if __name__ =='__main__':
    unittest.main()
