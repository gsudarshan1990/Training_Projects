"""
This is the automation test script
"""

from selenium import webdriver
import selenium
from Download_From_Lenovo.lenovo_page import LenovoPage
import time

browser = webdriver.Chrome("E:\chrome driver\chromedriver_win32\chromedriver.exe")
browser.maximize_window()
browser.implicitly_wait(10)
lenovopage = LenovoPage(browser)
lenovopage.go()
lenovopage.bios_uefi.click
biosuefipage = lenovopage.bios_click(browser)
biosuefipage.uefi_firmware_name.click
element =browser.find_element_by_xpath("//*[@id='app-psp-downloads']/section/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/ul/li[4]/a")
biosuefipage.mouse_click(element)
time.sleep(10)
browser.quit()
