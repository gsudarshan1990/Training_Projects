"""
This represents the BasePage of all the webpages
"""
from Selenium_With_Unittest.PageObjectModelWithUnittest.baseelement import BaseElement

class BasePage(BaseElement):
    """
    This represents the bage of all the pages
    """
    url = None
    def __init__(self,driver):
        """
        This is used to initialize the values
        :param driver: arg1 and representing the driver
        """
        self.driver = driver

    def go(self):
        """
        This is used to migrate to the given webpage
        :return: Nothing
        """
        self.driver.get(self.url)

    def moved_page(self):
        """
        This is used to provide details about the migrated page
        :return: Title of the migrated Page
        """
        return self.driver.current_url
