"""
This is used to test the application
"""

from selenium import webdriver
import selenium
from Page_Object_Model3_Amazon.Amazon_Page import AmazonPage
import time

browser = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe")
browser.maximize_window()
amapage = AmazonPage(browser)
amapage.go()
amapage.searchboxinput1.enter_text('Mobiles')
amapage.searchboxclick.click()
time.sleep(20)
browser.quit()