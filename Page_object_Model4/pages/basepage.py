"""
This class represents the Base Page
"""

class BasePage:
    """
    This is the base page of all the webpages
    """
    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)