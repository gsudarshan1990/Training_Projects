"""
Here we provide the definition of the class which describes about the WebElement
"""


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseElement:
    """
    Here We describe about the element of the class
    """
    def __init__(self, driver, by, value):
        self.driver = driver
        self.by = by
        self.value = value
        self.locator = (self.by,self.value)
        self.webelement = None
        self.find()

    @property
    def find(self):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator=self.locator))
        self.webelement = element
        return None

    @property
    def element_click(self):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator=self.locator))
        element.click()
        None

    @property
    def attribute(self,attr_value):
        return self.webelement.get_attribute(attr_value)

    @property
    def element_text(self):
        text = self.webelement.text
        return text

    def input_text(self, input_value):
        self.webelement.send_keys(input_value)
        return None
