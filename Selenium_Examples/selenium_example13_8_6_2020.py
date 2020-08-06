"""
This is an example of selenium which tests the title
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts =Options()
opts.headless = True

driver = webdriver.Chrome(options=opts,executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")

try:
    driver.get('http://webcode.me')
    assert 'My html page' == driver.title
finally:
    driver.quit()