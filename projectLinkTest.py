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


class ProjectLinkTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()


    def test_project_link(self):
        #Note this can only be tested on production not in web
         
        self.driver.get('http://linuxjobber.com/users/login')
        username = parser.get('linuxjobber.com/users/login', 'username')
        password = parser.get('linuxjobber.com/users/login', 'password')
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_xpath(".//*[@type='submit']").click()
        self.driver.find_element_by_link_text('Projects').click()
        self.driver.find_element_by_xpath("html/body/div[2]/div/div/a/h5").click()
        self.driver.find_element_by_xpath("html/body/section[2]/section/div/div/div[2]/a/button").click()
        


    def tearDown(self):

        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()