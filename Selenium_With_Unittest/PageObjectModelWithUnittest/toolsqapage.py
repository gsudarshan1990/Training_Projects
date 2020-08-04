"""
This represents the tools QA Page
"""

from Selenium_With_Unittest.PageObjectModelWithUnittest.basepage import BasePage
from selenium.webdriver.common.by import By
from Selenium_With_Unittest.PageObjectModelWithUnittest.baseelement import BaseElement
from Selenium_With_Unittest.PageObjectModelWithUnittest.blogspage import Blog

class Tools_QA(BasePage):
    """
    This represents the TOOlS_QA Page
    """
    def __init__(self, driver):
        self.driver = driver


    @property
    def blogs(self):
        """
        This represents the blogs on the home page
        :return: Nothing
        """
        locator1 = (By.XPATH,"//nav//a[@href='https://www.toolsqa.com/category/blogs/']//span[text()='Blogs']")
        return BaseElement(self.driver,locator1[0],locator1[1])

    def blog_click(self):
        """
        This returns the blogpage object
        :return: BlogPage Object
        """
        return Blog(driver=self.driver)