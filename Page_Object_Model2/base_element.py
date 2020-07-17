"""
This consists of class which represents the element on the page
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium

class BaseElement:
    def __init__(self, driver, by,value):
        """
        This initializes the values
        :param driver: arg1 and is driver which runs chrome
        :param value: arg2 and is element value
        :param by: arg3 and is element locator
        """
        self.driver = driver
        self.value = value
        self.by = by
        self.locator = (self.by, self.value)
        self.webElement = None

    def find(self):
        """
        This finds the element on the webpage
        :return: Nothing is returned
        """

        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        self.webElement = element
        return None

    def click(self):
        """
        This clicks the element which is found
        :return: Nothing is returned
        """
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator = self.locator))
        element.click()
        return None

