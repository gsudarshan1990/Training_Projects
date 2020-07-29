"""
Below Represents the Trail Page
"""

from .basepage import BasePage
from .baseelement import BaseElement
from selenium.webdriver.common.by import By

class TrailPage(BasePage):
    url = 'https://techstepacademy.com/trial-of-the-stones'

    @property
    def riddle_stone_text(self):
        locator2 = (By.XPATH,"//input[@id ='r1Input']")
        return BaseElement(self.driver, locator2[0],locator2[1])

    @property
    def riddle_stone_answer_button(self):
        locator3 = (By.CSS_SELECTOR, "button#r1Btn")
        return BaseElement(self.driver, locator3[0],locator3[1])

    @property
    def riddle_answer_text(self):
        locator4 = (By.XPATH, "//div[@id='passwordBanner']/h4")
        return BaseElement(self.driver, locator4[0],locator4[1])

    @property
    def riddle_secret_text(self):
        locator5 = (By.CSS_SELECTOR, "input#r2Input")
        return BaseElement(self.driver, locator5[0],locator5[1])

    @property
    def riddle_secret_answer_button(self):
        locator6 = (By.CSS_SELECTOR, "button#r2Butn")
        return BaseElement(self.driver, locator6[0],locator6[1])

    @property
    def merchant_answer_text(self):
        locator7 = (By.CSS_SELECTOR, "input#r3Input")
        return BaseElement(self.driver, locator7[0],locator7[1])

    @property
    def merchant_answer_button(self):
        locator8 = (By.CSS_SELECTOR, "button#r3Butn")
        return BaseElement(self.driver, locator8[0],locator8[1])
