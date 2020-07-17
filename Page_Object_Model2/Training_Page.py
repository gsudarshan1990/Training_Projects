"""
This class represents the page in the readable code
"""
from Page_Object_Model2.base_element import BaseElement
from selenium.webdriver.common.by import By

class TrainingPage(BaseElement):
    """
    This represents the page class
    """
    def __init__(self, driver):
        """
        This initializes the driver
        :param driver: arg1 and stirng
        """
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground'

    def go(self):
        """
        This renders to the given webpage
        :return: returns nothing
        """
        self.driver.get(self.url)

    @property
    def button(self):
        """
        This represents the element of the page
        :return: nothing
        """
        locator = (By.ID,'b1')
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def input_first(self):
        """
        This represents the first input text filed
        :return: element
        """
        locator1 = (By.ID, 'ipt1')
        return BaseElement(self.driver, locator1[0], locator1[0])