"""
This represents the lenovo page in the readable code format
"""

from Download_From_Lenovo.base_element import BaseElement
from selenium.webdriver.common.by import By
from Download_From_Lenovo.bios_uefi import Bios_Uefi

class LenovoPage(BaseElement):
    """
    This is the class which obtains contains the elements on the lenovo page
    """
    def __init__(self, driver):
        """
        This is used to initialize the variables
        :param driver: arg1 and driver
        """
        self.driver = driver
        self.url = 'https://datacentersupport.lenovo.com/in/en/products/servers/thinksystem/sr630/7x01/downloads/driver-list/'

    def go(self):
        """
        This is used to render the page
        :return: Nothing
        """
        self.driver.get(self.url)

    @property
    def bios_uefi(self):
        """
        This represents the bios element
        :return: Nothing
        """
        locator= (By.XPATH, "//div[@class ='text']//p[text()='BIOS/UEFI']")
        return BaseElement(self.driver, locator[0], locator[1])

    def bios_click(self,driver):
        return Bios_Uefi(driver)