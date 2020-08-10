"""
This is an example of the selenium with unittest which elaborates on the alerts
"""
import time

from selenium import webdriver
import unittest
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

class AlertTest(unittest.TestCase):
    """This class is used to test the alerts"""
    def setUp(self):
        """This is used to setup the browser for testing"""
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get('https://chandanachaitanya.github.io/selenium-practice-site/?languages=Java&enterText=')

    def test_alerts(self):
        """This is used to test different types of alerts"""
        self.driver.find_element(By.ID,"alertBox").click()
        ac = Alert(self.driver)
        ac.accept()
        time.sleep(1)
        self.driver.find_element(By.ID,"confirmBox").click()
        ac = Alert(self.driver)
        ac.accept()
        time.sleep(1)
        self.driver.find_element(By.ID, "confirmBox").click()
        ac = Alert(self.driver)
        ac.dismiss()
        time.sleep(1)
        self.driver.find_element(By.ID,"promptBox").click()
        ac = Alert(self.driver)
        ac.text ='chrome'
        time.sleep(2)
        ac.accept()

    def tearDown(self):
        """This is used for closing the browser"""
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()