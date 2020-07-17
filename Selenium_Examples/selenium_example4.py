"""
This is another example of selenium using the xpath
"""

from selenium import webdriver
import selenium

browser = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe")
browser.get('https://techstepacademy.com/training-ground')
browser.maximize_window()
input_xpath_element = "//input[@id ='ipt1']"
button_xpath_element = "//button[@id='b1']"
input_element = browser.find_element_by_xpath(input_xpath_element)
input_element.send_keys('My First Automation')
button = browser.find_element_by_xpath(button_xpath_element)
button.click()
