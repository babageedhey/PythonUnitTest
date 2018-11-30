import os
import time
import unittest
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

parser = ConfigParser()
options = webdriver.ChromeOptions()

parser.read("credentials.ini")

class TryFree(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()

    def test_try_free_guest(self):
        
        self.driver.get('http://54.149.10.37:8005')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('TRY FREE').click()
        time.sleep(3)
        #Go to login page to register or login
        self.assertIn('http://54.149.10.37:8005/login', self.driver.current_url)


    def test_try_free_user_page_state(self):
        self.test_try_free_guest()
        username = parser.get('http://54.149.10.37:8005', 'username')
        password = parser.get('http://54.149.10.37:8005', 'password')
        self.driver.find_element_by_id('formGroupExampleInput').send_keys(username)
        self.driver.find_element_by_id('formGroupExampleInput2').send_keys(password)
        self.driver.find_element_by_xpath(".//*[@type='submit']").click()
        #Check if it returns after login to trypage pay
        self.assertEquals('http://54.149.10.37:8005/tryfree/14daysPlan/', self.driver.current_url)


    def test_try_free_user(self):
        self.test_try_free_user_page_state()
        self.driver.find_element_by_link_text('Pay with Card').click()
        card_number = parser.get('card deatils', 'number')
        date = parser.get('card details', 'date')
        cvv = parser.get('card details', 'cvv')
        self.driver.find_element_by_id('11d44f00-f306-11e8-a9cc-3b786549ab2a').send_keys(card_number)
        self.driver.find_element_by_id('11d53960-f306-11e8-a9cc-3b786549ab2a').send_keys(date)
        self.driver.find_element_by_id('11d5ae90-f306-11e8-a9cc-3b786549ab2a').send_keys(cvv)
        self.driver.find_elements_by_css_selector('button').click()
        






    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
