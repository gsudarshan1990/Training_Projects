"""
This is another example of selenium with iframes

"""

from selenium import webdriver
import selenium

opts= webdriver.ChromeOptions()
opts.add_argument('--disable-gpu')
browser = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe",options = opts)
browser.get('https://techstepacademy.com/iframe-training')
browser.maximize_window()
iframe = browser.find_element_by_css_selector('iframe')
browser.switch_to.frame(iframe)
iframe_text_css_value = 'div#block-ec928cee802cf918d26c div p'
iframe_text_css_element = browser.find_element_by_css_selector(iframe_text_css_value)
print(iframe_text_css_element.text)
input_text_css_value= "input[id = 'ipt1']"
button_css_value = "button[id = 'b1']"
input_second_text_css_value = "input[id = 'ipt2']"
button_second_css_value = "button[id ='b2']"
input_element = browser.find_element_by_css_selector(input_text_css_value)
input_element.send_keys('My IFrame First Automation')
button_element = browser.find_element_by_css_selector(button_css_value)
input_second_element = browser.find_element_by_css_selector(input_second_text_css_value)
input_second_element.send_keys("Test Test")
button_element.click()
button_second_element = browser.find_element_by_css_selector(button_second_css_value)
button_second_element.click()
browser.switch_to.default_content()