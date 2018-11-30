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
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()

    def test_work_experience_entry(self):

            # user = int(input("--------To run test as anonymous user press 0 and hit enter-------- \n --------To run test as an unanonymous user press 1 and hit enter--------: "))
        self.driver.get("http://web.linuxjobber.com/users/login")#navigate to linuxjobber.com
        self.driver.implicitly_wait(5)
        username = parser.get('web.linuxjobber.com/users', 'username')
        password = parser.get('web.linuxjobber.com/users', 'password')
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_xpath(".//*[@type='submit']").click()
        self.driver.find_element_by_link_text("Work Experience").click()
        self.driver.find_element_by_xpath(".//*[@class='abouttext4']//a[1]").click()   
                   
                    #Test fails here, user is suppose to see payment page as soon as login is successful.
        self.driver.find_element_by_class_name('stripe-button-el').click()
        self.driver.switch_to.frame("stripe_checkout_app")
        self.driver.implicitly_wait(1)
        cardnumber = parser.get('web.linuxjobber.com/users', 'cardnumber')
        date = parser.get('web.linuxjobber.com/users', 'date')
        cvc = parser.get('web.linuxjobber.com/users', 'cvc')
        self.driver.find_element_by_xpath("//*[@placeholder='Card number']").send_keys(cardnumber)
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath("//*[@placeholder='MM / YY']").send_keys(date)
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath("//*[@placeholder='CVC']").send_keys(cvc)
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath("//*[@type='submit']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text("Proceed to agreement page").click()
        self.assertEqual("https://leif.org/commit?product_id=5b30461fe59b74063647c483#/", self.driver.current_url, "Payment Successful")        
    
    # def test_work_experience_senior(self):
    #     self.driver.get("http://web.linuxjobber.com/users/login")#navigate to linuxjobber.com
    #     self.driver.implicitly_wait(20)
    #     username = parser.get('web.linuxjobber.com/users/login', 'username')
    #     password = parser.get('web.linuxjobber.com/users/login', 'password')
    #     self.driver.find_element_by_id('username').send_keys(username)
    #     self.driver.find_element_by_id('password').send_keys(password)
    #     self.driver.find_element_by_xpath(".//*[@type='submit']").click()
    #     self.driver.find_element_by_link_text("Work Experience").click()
    #     self.driver.find_element_by_xpath(".//*[@class='abouttext3']//a[1]").click()   
                   
                    
    #     self.driver.find_element_by_class_name('stripe-button-el').click()
    #     self.driver.switch_to.frame("stripe_checkout_app")
    #     self.driver.implicitly_wait(1)
    #     cardnumber = parser.get('web.linuxjobber.com/users', 'cardnumber')
    #     date = parser.get('web.linuxjobber.com/users', 'date')
    #     cvc = parser.get('web.linuxjobber.com/users', 'cvc')
    #     self.driver.find_element_by_xpath("//*[@placeholder='Card number']").send_keys(cardnumber)
    #     self.driver.implicitly_wait(1)
    #     self.driver.find_element_by_xpath("//*[@placeholder='MM / YY']").send_keys(date)
    #     self.driver.implicitly_wait(1)
    #     self.driver.find_element_by_xpath("//*[@placeholder='CVC']").send_keys(cvc)
    #     self.driver.implicitly_wait(1)
    #     self.driver.find_element_by_xpath("//*[@type='submit']").click()
    #     self.driver.implicitly_wait(1)
    #     self.driver.find_element_by_link_text("Proceed to agreement page").click()
    #     self.assertEqual("https://leif.org/commit?product_id=5b30461fe59b74063647c483#/", self.driver.current_url, "Payment Successful")

            
    # def tearDown(self):
    #     time.sleep(8)
    #     self.driver.implicitly_wait(60)
    #     # self.driver.quit()



if __name__ == '__main__':
    unittest.main()