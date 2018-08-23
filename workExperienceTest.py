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

def test_login_auto(self):

    self.driver.get("http://web.linuxjobber.com/users/login")#navigate to linuxjobber.com
    self.driver.implicitly_wait(20)
    username = parser.get('web.linuxjobber.com/users/login', 'username')
    password = parser.get('web.linuxjobber.com/users/login', 'password')
    self.driver.find_element_by_id('username').send_keys(username)
    self.driver.find_element_by_id('password').send_keys(password)
    self.driver.find_element_by_xpath(".//*[@type='submit']").click()


class WorkExperienceTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\Jide\Desktop\Training\Projects\Linux\LinuxJobber\chromedriver.exe")
        self.driver.maximize_window()


    # def test_work_experience_entry(self):

    #         # user = int(input("--------To run test as anonymous user press 0 and hit enter-------- \n --------To run test as an unanonymous user press 1 and hit enter--------: "))
    #     self.driver.get("http://web.linuxjobber.com/users/login")#navigate to linuxjobber.com
    #     self.driver.implicitly_wait(20)
    #     username = parser.get('web.linuxjobber.com/users/login', 'username')
    #     password = parser.get('web.linuxjobber.com/users/login', 'password')
    #     self.driver.find_element_by_id('username').send_keys(username)
    #     self.driver.find_element_by_id('password').send_keys(password)
    #     self.driver.find_element_by_xpath(".//*[@type='submit']").click()
    #     self.driver.find_element_by_link_text("Work Experience").click()
    #     self.driver.find_element_by_xpath(".//*[@class='abouttext4']//a[1]").click()   
                   
    #                 #Test fails here, user is suppose to see payment page as soon as login is successful.
    #     self.driver.find_element_by_class_name('stripe-button-el').click()
    #     self.driver.switch_to.frame("stripe_checkout_app")
    #     self.driver.find_element_by_xpath("//*[@type='tel']").send_keys("42424242424242424")
    #     self.driver.find_element_by_xpath("//*[@placeholder='MM / YY']").send_keys("1219")
    #     self.driver.find_element_by_xpath("//*[@placeholder='CVC']").send_keys("1234")
    #     self.driver.find_element_by_xpath("//*[@type='submit']").click()
    #     self.driver.find_element_by_link_text("Proceed to agreement page").click()
                
    def test_work_experience_senior(self):
        self.driver.get("http://web.linuxjobber.com/users/login")#navigate to linuxjobber.com
        self.driver.implicitly_wait(20)
        username = parser.get('web.linuxjobber.com/users/login', 'username')
        password = parser.get('web.linuxjobber.com/users/login', 'password')
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_xpath(".//*[@type='submit']").click()
        self.driver.find_element_by_link_text("Work Experience").click()
        self.driver.find_element_by_xpath(".//*[@class='abouttext3']//a[1]").click()   
                   
                    #Test fails here, user is suppose to see payment page as soon as login is successful.
        self.driver.find_element_by_class_name('stripe-button-el').click()
        self.driver.switch_to.frame("stripe_checkout_app")
        self.driver.find_element_by_xpath("//*[@type='tel']").send_keys("42424242424242424")
        self.driver.find_element_by_xpath("//*[@placeholder='MM / YY']").send_keys("1219")
        self.driver.find_element_by_xpath("//*[@placeholder='CVC']").send_keys("1234")
        self.driver.find_element_by_xpath("//*[@type='submit']").click()
        self.driver.find_element_by_link_text("Proceed to agreement page").click()

            
    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()