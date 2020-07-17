"""
This is third example of selenium using the css selector
"""

from selenium import webdriver
import selenium

browser = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe")
browser.get('https://techstepacademy.com/training-ground')
browser.maximize_window()
input_element = browser.find_element_by_css_selector("input[id='ipt1']")
input_element.send_keys('My First Automation')
button = browser.find_element_by_css_selector("button[id = 'b1']")
button.click()
