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


parser.read("credentials.ini")

class AccountSettingTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\Jide\Desktop\Training\Projects\Linux\LinuxJobber\chromedriver.exe")
        self.driver.maximize_window()

    def test_account_settings_user(self):
        #LOgin First
        self.driver.get("http://web.linuxjobber.com/users/login")#navigate to linuxjobber.com
        self.driver.implicitly_wait(20)
        username = parser.get('web.linuxjobber.com/users/login', 'username')
        password = parser.get('web.linuxjobber.com/users/login', 'password')
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_xpath(".//*[@type='submit']").click()
            
        self.driver.find_element_by_xpath(".//*[@id='header']/div/div/div/div[3]/nav/ul/li/a").click()
        self.driver.find_element_by_xpath(".//*[@id='profile']/div/div[1]/ul/li[2]/a").click()
        self.driver.find_element_by_xpath(".//*[@class='video-study']/div/div/p/iframe").click()
        time.sleep(5)
        self.driver.find_element_by_name("data[csvfile]").send_keys("C:\\Users\\Jide\\Downloads\\accessKeys.csv")
        self.driver.find_element_by_xpath("html/body/div[2]/div/section[1]/div/div/div/form/button").click()
        self.driver.find_element_by_xpath("html/body/div[2]/div/section[3]/div/div").click()
        self.assertEqual("http://web.linuxjobber.com/users/accountSetting", self.driver.current_url)

    def test_upload_credentials(self):
        #Login First
        self.driver.get("http://web.linuxjobber.com/users/login")#navigate to linuxjobber.com
        self.driver.implicitly_wait(20)
        username = parser.get('web.linuxjobber.com/users/login', 'username')
        password = parser.get('web.linuxjobber.com/users/login', 'password')
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_xpath(".//*[@type='submit']").click()

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("html/body/header/div/div/div/div[3]/nav/ul/li/a").click()
        self.driver.find_element_by_xpath("html/body/header/div/div/div/div[3]/nav/ul/li/div/div/div/ul/li[2]/a").click()
        self.driver.find_element_by_xpath(".//*[@type='file']").send_keys("C:\\Users\\Jide\\Downloads\\jide_credentials.csv")#Pull the key from local computer
        self.driver.find_element_by_xpath(".//*[@class='form-horizontal']/button").click()
        upload_message = self.driver.find_element_by_id("flashMessage").text
        print (upload_message)   
        self.assertEqual("AWS credentials have been uploaded successfully", upload_message)
    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()