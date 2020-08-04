"""
This represents the blogs page
"""

from Selenium_With_Unittest.PageObjectModelWithUnittest.basepage import BasePage
from selenium.webdriver.common.by import By
from Selenium_With_Unittest.PageObjectModelWithUnittest.baseelement import BaseElement

class Blog(BasePage):
    """
    This represents the blogs Page
    """
    def __init__(self, driver):
        self.driver = driver

    @property
    def gitbranch(self):
        """
        This represents the Gitbranching sub menu on the page
        :return:gitbranch element
        """
        locator2 = (By.XPATH, "//div[contains(@class,'blog-media')])[4]//p//a")
        return BaseElement(self.driver,locator2[0],locator2[1])

