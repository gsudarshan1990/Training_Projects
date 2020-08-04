"""
This is used to test the POM using selenium unittest
"""


from selenium import webdriver
import unittest
from Selenium_With_Unittest.PageObjectModelWithUnittest.toolsqapage import Tools_QA
import time

class AutoTest(unittest.TestCase):
    """
    This is used to text the class
    """
    def setUp(self):
        """
        This is used for setting up the test
        :return: Nothing
        """
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()

    def test_toolsqa(self):
        """
        This is used to test the toolsqa
        :return: Nothing
        """
        tools_qa_object = Tools_QA(driver=self.driver)
        tools_qa_object.url = "https://www.toolsqa.com/"
        tools_qa_object.go()
        tools_qa_object.blogs.click
        self.assertEqual(self.driver.title, 'Blogs Archives | TOOLSQA')
        blog_page_object = tools_qa_object.blog_click()
        blog_page_object.gitbranch.mouse_move()
        blog_page_object.gitbranch.click
        self.assertEqual(self.driver.title,"What is the best suggested Git Branching Strategy for QA Automation?")


    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()