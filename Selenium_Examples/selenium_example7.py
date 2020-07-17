"""
This is another example of selenium using the xpath
"""

from selenium import webdriver
import selenium

browser = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe")
browser.get('https://techstepacademy.com/training-ground')
browser.maximize_window()
input_xpath_element = "//input[@id='ipt2']"
button_xpath_element = "//button[@id='b4']"
input_element = browser.find_element_by_xpath(input_xpath_element)
button_xpath_element = browser.find_element_by_xpath(button_xpath_element)
input_element.send_keys('Text Text')
button_xpath_element.click()
