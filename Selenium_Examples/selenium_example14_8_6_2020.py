"""
This is an example of the selenium which tests the pagesource
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.headless = True

driver = webdriver.Chrome(options=opts,executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")

try:
    driver.get('http://webcode.me')
    content = driver.page_source
    assert 'Today is a beautiful day' in content
finally:
    driver.quit()
