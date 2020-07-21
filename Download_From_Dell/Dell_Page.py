"""
This is the program which represents the Dell webpage in readable code format
"""

from Download_From_Dell.base_element import BaseElement
from selenium.webdriver.common.by import By


class DellPage(BaseElement):
    """
    Dell Page is represented in the code format
    """
    def __init__(self, driver):
        """
        This initializes the value
        :param driver: arg1 and is driver
        """
        self.driver = driver
        self.url = 'https://www.dell.com/support/home/in/en/inbsd1/product-support/product/poweredge-r640/drivers'

    def go(self):
        """
        This is used to move to the webpage
        :return: Nothing
        """
        self.driver.get(self.url)

    @property
    def name1(self):
        """
        This is the name of the element which is downloaded
        :return: nothing
        """
        locator1 = (By.XPATH, "(//div[@class='dl-desk-view'])[1]")
        return BaseElement(self.driver, locator1[0], locator1[1])

    @property
    def download1(self):
        """
        This is the element which should be downloaded
        :return: element in class format
        """
        locator2 = (By.XPATH,"//a[@id = 'btnDwn-RTWM9'][text()='Download']")
        return BaseElement(self.driver, locator2[0], locator2[1])

    @property
    def closecookie(self):
        """
        This is used to close the cookie
        :return: element in class format
        """
        locator3 = (By.ID, '_evidon-accept-button')
        return BaseElement(self.driver, locator3[0], locator3[1])