"""
This is used to represent the base element on the webpage
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC

class BaseElement:
    """
    This represents the webelement on the webpage
    """
    def __init__(self, driver, by, value):
        """
        This is used to initialize the values
        :param driver: arg1 and driver
        :param by: arg2 and type of by locator
        :param value: arg3 and type of value
        """
        self.driver = driver
        self.by = by
        self.value = value
        self.locator = (self.by,self.value)
        self.webelement = None
        self.find()

    def find(self):
        """
        This is used to find the element on the webpage
        :return: Nothing
        """
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator=self.locator))
        self.webelement = element
        return None

    @property
    def click(self):
        """
        This is used to click the element
        :return: Nothing
        """
        element = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    def text(self):
        """
        This is used to return text from the element
        :return: text in the form of string
        """
        text1 = self.webelement.text
        return text1

    def mouse_move(self):
        """
        This mouse to the corresponding element on the webpage
        :return: Nothing
        """
        AC(self.driver).move_to_element(self.webelement).perform()

