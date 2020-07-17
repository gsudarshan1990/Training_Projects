"""
This is the example of selenium
"""

from selenium import webdriver
import selenium

browser = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe")
browser.get("https://www.google.com")
