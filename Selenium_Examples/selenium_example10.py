"""
This is another example of selenium with multiple tabs on browser

"""

from selenium import webdriver
import selenium

opts = webdriver.ChromeOptions()
opts.add_argument('--disable-gpu')
browser = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe", options = opts)
browser.execute_script('window.open("https://www.google.com","_blank");')
browser.execute_script('window.open("https://www.yahoo.com","_blank");')
browser.execute_script('window.open("https://www.ebay.com","_blank");')
browser.execute_script('window.open("https://techstepacademy.com/","_blank");')

print(len(browser.window_handles))