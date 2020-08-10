"""
This is an example of selenium along with the unittest testing the webtable
"""

from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class WebTableUnitTest(unittest.TestCase):
    """This class is used to test the webtable of the webpage"""
    def setUp(self):
        """This is used to set up the browser for testing"""
        self.driver = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get('https://www.w3schools.com/html/html_tables.asp')

    def test_1_Rows(self):
        """This is used to test the rows"""
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(locator = (By.CLASS_NAME,"w3-example")))
        num_of_rows = len(self.driver.find_elements_by_xpath("//*[@id='customers']//tbody//tr"))
        print(num_of_rows)

    def test_2_Columns(self):
        """This is used to test the columns"""
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(locator=(By.CLASS_NAME,"w3-example")))
        num_of_columns = len(self.driver.find_elements_by_xpath("//*[@id='customers']//tbody//tr[2]//td"))
        print(num_of_columns)

    def tearDown(self):
        """This is used to close the browser"""
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()