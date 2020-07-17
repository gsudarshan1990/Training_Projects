"""
This is another example of selenium with window handles and switching
"""

from selenium import webdriver
import selenium

opts = webdriver.ChromeOptions()
opts.add_argument('--disable-gpu')
browser = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe", options = opts)
browser.execute_script('window.open("https://www.google.com","_blank");')
browser.execute_script('window.open("https://www.yahoo.com", "_blank");')
browser.execute_script('window.open("https://www.ebay.com", "_blank");')
browser.execute_script('window.open("https://www.msystechnologies.com/","_blank");')

handles = browser.window_handles
browser.switch_to.window(handles[2])