"""
This is the page which represents the element on the webpage
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC


class BaseElement:
    """
    This is the class which represents the element
    """
    def __init__(self, driver, by, value):
        """
        This is used to initialize the value
        :param driver: arg1 which represents the driver
        :param by: arg2 which represents the type of locator
        :param value: arg3 which represents the value of locator
        """
        self.driver = driver
        self.by = by
        self.value = value
        self.locator = (self.by, self.value)
        self.webelement = None



    def find(self):
        """
        This is used to find the web element value
        :return: Nothing
        """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        self.webelement = element
        return None

    @property
    def click(self):
        """
        This is used to click the element
        :return: nothing
        """
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator = self.locator))
        element.click()
        return None

    @property
    def text(self):
        """
        This is used to return text present on the webelement
        :return: text as string
        """
        return self.webelement.text

    def mouse_click(self, element1):
        """
        This is used to move to the element on the webpage and click the element
        :param element1: arg1 and the webelement
        :return: Nothing
        """
        AC(self.driver).move_to_element(element1).click(element1).perform()
        return None


