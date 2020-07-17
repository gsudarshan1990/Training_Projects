"""
This is the class which represents the webelement in the code readable
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseElement:
    """
    This represents the element
    """
    def __init__(self, driver, by, value):
        """
        This initializes the values
        :param driver: arg1 and webdriver
        :param by: arg2 and the by element
        :param value: arg3 and the value
        """
        self.driver = driver
        self.by = by
        self.value = value
        self.locator = (self.by, self.value)
        self.webelement = None

    def find(self):
        """
        This is used to find the element
        :return:
        """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        self.webelement = element
        return None

    def click(self):
        """
        This is used to click the element
        :return:
        """
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator = self.locator))
        self.webelement= element
        self.webelement.click()
        return None

    def is_visible(self):
        """
        This is check whether element is visible
        :return: returns the boolean value
        """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator = self.locator))
        self.webelement = element
        return bool(self.webelement)

    def is_enabled(self):
        """
        This is used to check whether element is enabled
        :return: returns the boolean value
        """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator = self.locator))
        self.webelement = element
        return self.webelement.isEnabled()

    def enter_text(self, text):
        """
        This is used to enter the text
        :param text: arg1 and text to enter into the element
        :return: nothing
        """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator = self.locator))
        self.webelement = element
        self.webelement.send_keys(text)
        return None