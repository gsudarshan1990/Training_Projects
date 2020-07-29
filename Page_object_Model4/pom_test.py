"""
This represents the Page Object Model representation
"""

from selenium import webdriver
import selenium
from Page_object_Model4.pages.Training_Page import TrainingPage
from Page_object_Model4.pages.Trail_Page import TrailPage

browser = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe")
browser.implicitly_wait(10)
browser.maximize_window()
trng_page = TrainingPage(driver = browser)
trng_page.go()



trail_page = TrailPage(driver= browser)
trail_page.go()
trail_page.riddle_stone_text.input_text('rock')

