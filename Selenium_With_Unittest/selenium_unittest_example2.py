"""
This is another example of the selenium using the explicit wait using the unittest
"""

from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

class ExplictWaitTest(unittest.TestCase):
    """
    This class is used to test the unittest case
    """
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.base_url = "https://www.google.com/"
        self.driver.maximize_window()
        #self.locator1 = (By.ID,'q') obtains the TimeOutException
        self.locator1 = (By.NAME, 'q')

    def test_search(self):
        self.driver.get(self.base_url)
        try:
            element_id = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator=self.locator1))
            element_id.send_keys('Selenium')
            element_id.send_keys(Keys.ENTER)
        except TimeoutException:
            print('Exceeded the time')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
