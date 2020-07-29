"""
This represents the Training Page
"""
from .basepage import BasePage
from .baseelement import BaseElement
from selenium.webdriver.common.by import By

class TrainingPage(BasePage):

    url = 'https://techstepacademy.com/training-ground/'

    @property
    def button_one(self):
        locator1 = (By.ID ,"b1")
        return BaseElement(self.driver, locator1[0],locator1[1])