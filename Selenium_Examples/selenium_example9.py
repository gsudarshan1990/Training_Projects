"""
This is another example of selenium with two browsers
"""

from selenium import webdriver
import selenium

opts = webdriver.ChromeOptions()
opts.add_argument('--disable-gpu')
browser1 = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe",options=opts)
browser2 = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe",options=opts)
browser1.maximize_window()
browser2.maximize_window()
browser1.get('https://techstepacademy.com/training-ground')
browser2.get('https://www.google.com')