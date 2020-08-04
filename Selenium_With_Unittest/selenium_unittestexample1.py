"""
This is an example of selenium unittest
"""

from selenium import webdriver
import unittest
import time

class LoginTest(unittest.TestCase):
    """
    This class is used to text the login page of facebook
    """
    def setUp(self):
        """
        This is used to set up the
        :return:
        """
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.base_url = "https://github.com/"

    def test_login(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("user[login]").send_keys("sudarshan2030")
        self.driver.find_element_by_id("user[email]").send_keys('sudarshan@yahootechnologies.com')
        self.driver.find_element_by_id("user[password]").send_keys("123456378")
        self.driver.find_element_by_xpath("(//button[text()='Sign up for GitHub'])[1]").click()

    def tearDown(self):
        time.sleep(20)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()



