"""
This is used to download the page
"""

from selenium import webdriver
import selenium
from Download_From_Dell.Dell_Page import DellPage
import time

opts = webdriver.ChromeOptions()
opts.add_argument('--disable-gpu')
browser = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe", options=opts)
browser.maximize_window()
dellpage = DellPage(browser)
dellpage.go()
dellpage.closecookie.click
dellpage.download1.click
attribute_value = dellpage.download1.get_attribute_value('href')
words = attribute_value.split('/')
file_name = words[-1]
time.sleep(100)
browser.quit()