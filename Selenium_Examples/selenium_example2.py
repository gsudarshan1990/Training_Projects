"""
This is the second example of selenium
"""

from selenium import webdriver
import selectors

browser = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe")
browser.get('https://techstepacademy.com/training-ground')
input_element = browser.find_element_by_id('ipt1')
browser.maximize_window()
print(input_element)
input_element.send_keys("My First Automation Script")
button = browser.find_element_by_id('b1')
button.click()