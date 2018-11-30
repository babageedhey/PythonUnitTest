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

class RhcsaOrder(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()

    def test_rhcsa_order(self):
        #Login First
        self.driver.get("http://54.149.10.37:8005/login")#navigate to linuxjobber.com
        self.driver.implicitly_wait(20)
        username = parser.get('http://54.149.10.37:8005', 'username')
        password = parser.get('http://54.149.10.37:8005', 'password')
        self.driver.find_element_by_id('formGroupExampleInput').send_keys(username)
        self.driver.find_element_by_id('formGroupExampleInput2').send_keys(password)
        self.driver.find_element_by_xpath(".//*[@type='submit']").click()
        #Click the OrderPage ICon
        self.driver.find_element_by_xpath(".//*[@id='header']/div/div/div/div[3]/nav/ul/li/a").click()
        self.driver.find_element_by_link_text('RHCSA Order').click()
        self.driver.implicitly_wait(12)
        self.assertEqual('http://54.149.10.37:8005/user/RHCSA/order_details', self.driver.current_url)



    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()