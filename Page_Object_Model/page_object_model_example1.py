"""
This is the first example of page object model
"""

class TrainingPage:
    """
    This class represent the page https://techstepacademy.com/training-ground/ in the readable code
    """
    def __init__(self, driver):
        """
        This initializes the values
        :param driver: arg1 and string
        """
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground/'

    def go(self):
        """
        This opens the webpage
        :return:
        """
        self.driver.get(self.url)

    def type_into_element(self, element1, text_value):
        """
        This is used to enter the value into the input element
        :param element1: arg1 and webelement
        :return: nothing
        """
        input_element = self.driver.find_element_by_css_selector(element1)
        input_element.clear()
        input_element.send_keys(text_value)
        return None

    def get_text(self, element1):
        """
        This is used to obtain the text from the element
        :return: text
        """
        input_element = self.driver.find_element_by_css_selector(element1)
        text = input_element.get_attribute('value')
        return text

    def click_button(self, button_element):
        """
        This is used to click the button
        :param button_element: arg1 and the webelement
        :return: nothing
        """
        button_element = self.driver.find_element_by_css_selector(button_element)
        button_element.click()
        return None


