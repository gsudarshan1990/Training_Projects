"""
This represents the bios_uefi page
"""
from Download_From_Lenovo.base_element import  BaseElement
from selenium.webdriver.common.by import By


class Bios_Uefi(BaseElement):
    """
    This is the class which represents the bios_uefi in the class format
    """
    def __init__(self, driver):
        """
        This initializes the values
        :param driver: arg1 and driver
        """
        self.driver = driver
        self.url = 'https://datacentersupport.lenovo.com/in/en/products/servers/thinksystem/sr630/7x01/downloads/driver-list/component?name=BIOS%2FUEFI'

    def go(self):
        """
        This is used to go the new url
        :return: Nothing
        """
        self.driver.get(self.url)

    @property
    def uefi_firmware_name(self):
        """
        This is the uefi_firmware name
        :return: uefi firmware element
        """
        locator = (By.XPATH, "//*[@id='app-psp-downloads']/section/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/ul/li[1]/p/strong")
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def uefi_firmware_download(self):
        """
        This is the uefi_firmware download element
        :return:returns the element in the class format
        """
        locator1 = (By.XPATH, "//*[@id='app-psp-downloads']/section/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/ul/li[4]/a")
        return BaseElement(self.driver, locator1[0], locator1[1])


