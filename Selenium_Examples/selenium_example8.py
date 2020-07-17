"""
This is another example of selenium using the css selector

"""

from selenium import webdriver
import selenium

browser = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe")
browser.get('https://techstepacademy.com/trial-of-the-stones')
browser.maximize_window()
input_css_riddle_of_stone_value = "input[id='r1Input']"
input_css_riddle_of_secret_value = "input[id='r2Input']"
two_merchant_xpath_value = "//b[text()='Jessica']"
button_css_riddle_of_stone_value = "button[id='r1Btn']"
button_css_riddle_of_secret_value = "button[id='r2Butn']"
input_css_merchant_value = "input[id='r3Input']"
button_css_answer_value = "button[id='r3Butn']"
button_css_check_answer_value = "button[id='checkButn']"
input_riddle_of_stone_element = browser.find_element_by_css_selector(input_css_riddle_of_stone_value)
input_riddle_of_secret_element = browser.find_element_by_css_selector(input_css_riddle_of_secret_value)
button_riddle_of_stone_element = browser.find_element_by_css_selector(button_css_riddle_of_stone_value)
button_riddle_of_secret_element = browser.find_element_by_css_selector(button_css_riddle_of_secret_value)
input_css_merchant_element = browser.find_element_by_css_selector(input_css_merchant_value)
two_merchant_xpath_element = browser.find_element_by_xpath(two_merchant_xpath_value)
button_css_answer_element = browser.find_element_by_css_selector(button_css_answer_value)
button_css_check_answer_element = browser.find_element_by_css_selector(button_css_check_answer_value)
input_riddle_of_stone_element.send_keys('rock')
button_riddle_of_stone_element.click()
riddle_stone_result_value = "//h4[text()='bamboo']"
riddle_stone_result_element= browser.find_element_by_xpath(riddle_stone_result_value)
input_riddle_of_secret_element.send_keys(riddle_stone_result_element.text)
button_riddle_of_secret_element.click()
input_css_merchant_element.send_keys(two_merchant_xpath_element.text)
button_css_answer_element.click()
button_css_check_answer_element.click()






