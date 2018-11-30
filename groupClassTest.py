import unittest
import time

import os

from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

parser = ConfigParser()
options = webdriver.ChromeOptions()

parser.read("credentials.ini")


class GroupTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()

    def test_login_auto(self):
        self.driver.get("http://web.linuxjobber.com/users/login")#navigate to linuxjobber.com
        self.driver.implicitly_wait(20)
        username = parser.get('web.linuxjobber.com/users/login', 'username')
        password = parser.get('web.linuxjobber.com/users/login', 'password')
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_xpath(".//*[@type='submit']").click()
        self.assertEqual("http://web.linuxjobber.com/tutorials/userinterest", self.driver.current_url)
        self.driver.implicitly_wait(10)
        time.sleep(8)
        
       

   
    def test_groupclass_guest_no_option(self):
        self.driver.get('http://web.linuxjobber.com')
        self.driver.find_element_by_link_text('Group Class').click()
        self.driver.find_element_by_xpath(".//*[@id='register']/button").click()
        time.sleep(5)

    def test_groupclass_guest_option(self):
        self.driver.get('http://web.linuxjobber.com')
        self.driver.find_element_by_link_text('Group Class').click()
        self.driver.find_element_by_xpath(".//*[@class='groupbox']/input").click()
        self.driver.find_element_by_xpath(".//*[@id='register']/button").click()
        time.sleep(5)

    def test_groupclass_user_no_option(self):
        self.test_login_auto()
        self.driver.find_element_by_link_text('Group Class').click()
        self.driver.find_element_by_xpath(".//*[@id='register']/button").click()
        time.sleep(5)

    def test_groupclass_user_option(self):
        self.test_login_auto()
        self.driver.find_element_by_link_text('Group Class').click()
        self.driver.find_element_by_xpath(".//*[@class='groupbox']/input").click()
        self.driver.find_element_by_xpath(".//*[@id='register']/button").click()
        time.sleep(5)

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()

          
if __name__ == '__main__':
    unittest.main()