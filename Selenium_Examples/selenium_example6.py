"""
This is another example of selenium
"""

from selenium import webdriver
import selenium

browser = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe")
browser.get('https://techstepacademy.com/training-ground')
browser.maximize_window()
input_css_element ="input[id='ipt2']"
button_css_element = "button[id='b4']"
input_element = browser.find_element_by_css_selector(input_css_element)
button_element = browser.find_element_by_css_selector(button_css_element)
input_element.send_keys('Text Text')
button_element.click()