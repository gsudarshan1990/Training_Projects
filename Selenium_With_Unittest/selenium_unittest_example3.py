"""
This is another example of the selenium with the parameterized test cases
"""

from selenium import webdriver
import unittest

class LoginTestWithParameters(unittest.TestCase):
    """
    This is the example of the unit test with the parameterization
    """
    def setUp(self):
        """
        This is used to setup the driver
        :return: Nothing
        """
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.base_url = 'https://github.com/'

    def test_git(self):
        """
        This is used to test the page with the multiple parameters
        :return: Nothing
        """
        self.driver.get(self.base_url)
        with open("E:\Training_Projects\credentials.txt", "r") as fileheader:
            for line in fileheader:
                line =line.strip()
                individual_data = line.split(',')
                self.driver.find_element_by_id("user[login]").send_keys(individual_data[0])
                self.driver.find_element_by_id("user[email]").send_keys(individual_data[1])
                self.driver.find_element_by_id("user[password]").send_keys(individual_data[2])
                self.driver.find_element_by_xpath("(//button[text()='Sign up for GitHub'])[1]").click()
                if (self.driver.current_url == 'https://github.com/join'):
                    print('Entered the new page')
                    self.driver.get("https://github.com/")
                else:
                    print('Entered the Incorrect Page')

    def tearDown(self):
        """
        This is used to quit the brower
        :return: Nothing
        """
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
