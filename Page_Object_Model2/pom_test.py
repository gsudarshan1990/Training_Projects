"""
This is the page which test the webpage
"""

from Page_Object_Model2.Training_Page import TrainingPage
from selenium import webdriver
import selenium

browser = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe")
browser.maximize_window()
trngpage = TrainingPage(driver=browser)
trngpage.go()
trngpage.button.click()




