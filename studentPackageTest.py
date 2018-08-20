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

class StudPackageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\Jide\Desktop\Training\Projects\Linux\LinuxJobber\chromedriver.exe")
        self.driver.maximize_window()

    def test_student_package_guest(self):
        self.driver.get('http://linuxjobber.com')
        self.driver.find_element_by_link_text('Student Packages').click()
        self.driver.find_element_by_xpath("html/body/div[2]/div[3]/div/div/div[1]/div/div[3]/a").click()
        #Fill Form here
        firstname = parser.get('web.linuxjobber.com/users/login', 'firstname')
        lastname = parser.get('web.linuxjobber.com/users/login', 'lastname')
        email = parser.get('web.linuxjobber.com/users/login', 'email')
        self.driver.find_element_by_id('fname').send_keys(firstname)
        self.driver.find_element_by_id('lname').send_keys(lastname)
        self.driver.find_element_by_id('email').send_keys(email)
        self.driver.find_element_by_name('submit').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_class_name("stripe-button-el").click()
        #fill the modal form        
        self.driver.switch_to.frame("stripe_checkout_app")
        self.driver.find_element_by_xpath("//*[@type='tel']").send_keys("42424242424242424")
        self.driver.find_element_by_xpath("//*[@placeholder='MM / YY']").send_keys("1219")
        self.driver.find_element_by_xpath("//*[@placeholder='CVC']").send_keys("123")
        self.driver.find_element_by_xpath("//*[@type='submit']").click()
        self.driver.implicitly_wait(10)
        message = self.driver.find_element_by_class_name("Popover-content")
        errorMessage = message.text
        self.assertIn("Your card was declined", errorMessage)
        
        time.sleep(5)   
       
    def test_student_package_user(self):
        #Login as a registered User
        self.driver.get("http://linuxjobber.com/users/login")#navigate to linuxjobber.com
        self.driver.implicitly_wait(20)
        username = parser.get('linuxjobber.com/users/login', 'username')
        password = parser.get('linuxjobber.com/users/login', 'password')
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_xpath(".//*[@type='submit']").click()
        #go to student packages
        self.driver.find_element_by_link_text('Student Packages').click()
        self.driver.find_element_by_xpath("html/body/div[2]/div[3]/div/div/div[1]/div/div[3]/a").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_class_name("stripe-button-el").click()
        self.driver.implicitly_wait(5)
        #fill the modal form        
        self.driver.switch_to.frame("stripe_checkout_app")
        self.driver.find_element_by_xpath("//*[@type='email']").send_keys("test12@gmail.com")
        self.driver.find_element_by_xpath("//*[@type='tel']").send_keys("42424242424242424")
        self.driver.find_element_by_xpath("//*[@placeholder='MM / YY']").send_keys("1219")
        self.driver.find_element_by_xpath("//*[@placeholder='CVC']").send_keys("123")
        self.driver.find_element_by_xpath("//*[@type='submit']").click()
        self.driver.implicitly_wait(10)
        message = self.driver.find_element_by_class_name("Popover-content")
        errorMessage = message.text
        self.assertIn("Your card was declined", errorMessage)
        
        time.sleep(5)     


    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()