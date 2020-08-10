"""
This is an example of the selenium with unitest using the iframes
"""

from selenium import webdriver
import unittest

class IFrameUnittest(unittest.TestCase):
    """This class is used to test the iframes with unittest"""
    def setUp(self):
        """This is used for setting up to perform the automation test"""
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://letskodeit.teachable.com/p/practice")

    def test_IFrame(self):
        """This is used for testing the IFrame"""
        print('Scroll Till the location')
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.switch_to.frame("courses-iframe")
        self.driver.find_element_by_id("search-courses").send_keys("python")
        self.driver.find_element_by_xpath("//i[@title='Search']").click()
        self.driver.switch_to.default_content()


    def tearDown(self):
        """This is used to close the browser"""
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

