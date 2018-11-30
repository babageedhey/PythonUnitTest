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


class UserTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()


    def test_user_signup(self):
        self.driver.get("http://web.linuxjobber.com")
        self.driver.implicitly_wait(20)
        fullname = parser.get('web.linuxjobber.com', 'fullname')
        username = parser.get('web.linuxjobber.com', 'email')
        password = parser.get('web.linuxjobber.com', 'password')
        self.driver.find_element_by_link_text("Sign Up").click()
        self.driver.find_element_by_id('fullname').send_keys(fullname)
        self.driver.find_element_by_id('email').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_xpath(".//*[@id='myform']/div[6]/button").click()
        self.driver.implicitly_wait(10)
        created = self.driver.find_element_by_id("flashMessage")
        usercreated = created.text
        print (usercreated)
        self.assertEqual("Account has been created. Please check your email", usercreated)
        time.sleep(8)


    def test_login_auto(self):
        self.driver.get("http://web.linuxjobber.com/users/login")#navigate to linuxjobber.com
        self.driver.implicitly_wait(20)
        username = parser.get('web.linuxjobber.com/users/login', 'username')
        password = parser.get('web.linuxjobber.com/users/login', 'password')
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_xpath(".//*[@type='submit']").click()
        self.driver.implicitly_wait(10)
        self.assertEqual("http://web.linuxjobber.com/tutorials/userinterest", self.driver.current_url)
        time.sleep(8)
        
       
    def test_password_recovery(self):
        self.driver.get("http://web.linuxjobber.com/users/login")
        self.driver.find_element_by_xpath(".//*[@id='UserLoginForm']//a[1]").click()
        email = parser.get("web.linuxjobber.com/users/login", 'email')
        self.driver.find_element_by_id("email").send_keys(email)
        self.driver.find_element_by_xpath(".//*[@type='submit']").click()
        self.driver.implicitly_wait(10)
        recoverysent = self.driver.find_element_by_id("flashMessage")
        messagesent = recoverysent.text
        print (messagesent)
        self.assertEqual("we have sent email to you. Please check email.", messagesent)
        time.sleep(8)

    

    


    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()

          
if __name__ == '__main__':
    unittest.main()



