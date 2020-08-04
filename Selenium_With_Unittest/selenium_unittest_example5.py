"""
This is the example of selenium unittest with frames
"""

from selenium import webdriver
import unittest

class FrameTest(unittest.TestCase):
    """
    This is used to test the frames
    """
    def setUp(self):
        """
        This is used for the setup of the driver
        :return: Nothing
        """
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.base_url = 'https://the-internet.herokuapp.com/nested_frames'

    def test_frames(self):
        """
        This is used to test the frames
        :return: Nothing
        """
        self.driver.get(self.base_url)
        self.driver.switch_to.frame(self.driver.find_element_by_name("frame-top"))
        self.driver.switch_to.frame(self.driver.find_element_by_name('frame-right'))
        print(self.driver.page_source)

    def tearDown(self):
        """
        This is used to close the project
        :return: Nothing
        """
        self.driver.quit()

if __name__ == '__main__':
    self.driver.quit()