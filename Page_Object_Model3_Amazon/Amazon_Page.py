"""
This is about representing the amazon page in the code readable format
"""

from Page_Object_Model3_Amazon.base_element import BaseElement
from selenium.webdriver.common.by import By

class AmazonPage(BaseElement):
    """
    This is class which represents in amazon page
    """
    def __init__(self, driver):
        """
        This is used initializing the values
        :param driver: arg1 and driver
        """
        self.driver = driver
        self.url = 'https://www.amazon.in/'

    def go(self):
        self.driver.get(self.url)

    @property
    def searchboxinput1(self):
        locator1 = (By.ID, 'twotabsearchtextbox')
        return BaseElement(self.driver, locator1[0], locator1[1])

    @property
    def searchboxclick(self):
        locator2 = (By.CSS_SELECTOR , "input[value='Go']")
        return BaseElement(self.driver , locator2[0], locator2[1])

