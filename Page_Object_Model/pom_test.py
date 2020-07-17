from selenium import webdriver
import selenium

from Page_Object_Model.page_object_model_example1 import TrainingPage

browser = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe")

trng_page = TrainingPage(browser)
trng_page.go()
input_css_element_value = "input[id = 'ipt1']"
text_value1 = 'text_value'
trng_page.type_into_element(input_css_element_value, text_value1)
text_value2 =trng_page.get_text(input_css_element_value)
assert text_value2 == text_value1 , f'Values Did not Match'
print('test passed')

