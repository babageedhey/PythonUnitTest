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


class ResumeTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()


    def test_resume_service(self):
        firstname = parser.get('web.linuxjobber.com/users/login', 'firstname')
        lastname = parser.get('web.linuxjobber.com/users/login', 'lastname')
        email = parser.get('web.linuxjobber.com/users/login', 'email')
        self.driver.get('http://web.linuxjobber.com')
        self.driver.find_element_by_link_text('Resume Services').click()
        self.driver.find_element_by_link_text('Buy Now').click()
        self.driver.find_element_by_id('fname').send_keys(firstname)
        self.driver.find_element_by_id('lname').send_keys(lastname)
        self.driver.find_element_by_id('email').send_keys(email)
        self.driver.find_element_by_id('btnpaynow').click()
        self.driver.implicitly_wait(10)
        time.sleep(8)


    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()