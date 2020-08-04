"""
This is another example of selenium with the unittest which is used to test the form
"""

from selenium import webdriver
import unittest
from selenium.webdriver.support.select import Select

class Registration(unittest.TestCase):
    """
    This is used to test the Registration form
    """
    def setUp(self):
        """
        This is used to setup the driver
        :return: Nothing
        """
        self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.base_url = 'http://demo.guru99.com/insurance/v1/register.php'

    def test_webpage(self):
        """
        This is used to test the webpage
        :return: Nothing
        """
        self.driver.get(self.base_url)
        select1 = Select(self.driver.find_element_by_id("user_title"))
        select1.select_by_value("Mr")
        self.driver.find_element_by_id("user_firstname").send_keys('sudar')
        self.driver.find_element_by_id('user_surname').send_keys('shan')
        self.driver.find_element_by_id('user_phone').send_keys('12345692892')
        Select(self.driver.find_element_by_id("user_dateofbirth_1i")).select_by_value("1947")
        Select(self.driver.find_element_by_id('user_dateofbirth_2i')).select_by_value("5")
        Select(self.driver.find_element_by_id('user_dateofbirth_3i')).select_by_value("19")
        isSelected = self.driver.find_element_by_id('licencetype_f').get_attribute('checked')
        if isSelected is None:
            self.driver.find_element_by_id('licencetype_f').click()
        else:
            self.driver.find_element_by_id('licencetype_t').click()
        Select(self.driver.find_element_by_id('user_licenceperiod')).select_by_value("3")
        Select(self.driver.find_element_by_id('user_occupation_id')).select_by_value("5")
        self.driver.find_element_by_id('user_address_attributes_street').send_keys('Chaitanyapuri')
        self.driver.find_element_by_id('user_address_attributes_city').send_keys('Hyd')
        self.driver.find_element_by_id('user_address_attributes_county').send_keys('Ind')
        self.driver.find_element_by_id('user_address_attributes_postcode').send_keys('500030')
        self.driver.find_element_by_id('user_user_detail_attributes_email').send_keys('sudarshan@yahoo.com')
        self.driver.find_element_by_id('user_user_detail_attributes_password').send_keys('12343532423')
        self.driver.find_element_by_id('user_user_detail_attributes_password_confirmation').send_keys('12343532423')
        self.driver.find_element_by_xpath("//input[@value='Create']").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()