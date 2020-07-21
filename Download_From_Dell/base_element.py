"""
This represents the Base element
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as ac

class BaseElement:
    """
    This is the class which represents element on the page
    """
    def __init__(self, driver, by, value):
        """
        This is used to initialize the values
        :param driver: arg1 and driver
        :param by: arg2 and represents the type of locator
        :param value: arg3 and represents the value of locator
        """
        self.driver = driver
        self.by = by
        self.value = value
        self.locator = (self.by, self.value)

        self.webelement = None

    def find(self):
        """
        This is used to find the element on the web page
        :return: Nothing
        """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        self.webelement = element
        return None

    @property
    def click(self):
        """
        This is used to click the selected webelement
        :return: Nothing
        """

        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    @property
    def mousemovementclick(self, element2):
        """
        This is used to click the element after the mouse movement
        :return: nothing
        """
        ac(driver=self.driver).move_to_element(element2).click(element2).perform()
        return None

    def get_attribute_value(self, attribute):
        """
        This returns the attribute value
        :return: string
        """
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator=self.locator))
        attribute_value =element.get_attribute(attribute)
        return attribute_value



    def text(self):
        """
        This provdies the text
        :return: the text
        """
        return self.webelement.text