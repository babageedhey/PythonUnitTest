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





class JobPlacementTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()
   
    def test_job_placement_user_entry_certificate(self):
        
        self.driver.get("http://web.linuxjobber.com/users/login")#navigate to linuxjobber.com
        self.driver.implicitly_wait(20)
        username = parser.get('web.linuxjobber.com/users/login', 'username')
        password = parser.get('web.linuxjobber.com/users/login', 'password')
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_xpath(".//*[@type='submit']").click()

        self.driver.find_element_by_xpath(".//*[@id='footer-row']/div[2]/ul/li[7]/a").click()    
        self.driver.find_element_by_xpath(".//*[@class='jp-content']/div/div/div/div/div/a").click()#Click the Entry Level Button
        first_name = parser.get('web.linuxjobber.com/users/login', 'firstname')
        last_name = parser.get('web.linuxjobber.com/users/login', 'lastname')
        email = parser.get('web.linuxjobber.com/users/login', 'email')
        self.driver.find_element_by_id('firstname').send_keys(first_name)
        self.driver.find_element_by_id('lastname').send_keys(last_name)
        self.driver.find_element_by_id('email').send_keys(email)
        self.driver.find_element_by_xpath(".//*[@id='education']/option[5]").click()
        self.driver.find_element_by_id('JobplacementsResume').send_keys("C:\\Users\\Jide\\Desktop\\Training\\Projects\\Linux\\LinuxJobber\\Goals.docx")
        self.driver.find_element_by_xpath(".//*[@id='app']/div[7]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='JobplacementsCareer']/option[8]").click()  
        #Certificate Form   
        self.driver.find_element_by_xpath(".//*[@id='JobplacementsCertification']/option[1]").click()
        self.driver.find_element_by_id('JobplacementsCertificate').send_keys("C:\\Users\\Jide\\Desktop\\Training\\Projects\\Linux\\LinuxJobber\\Goals.docx")  
        self.driver.find_element_by_xpath(".//*[@id='JobplacementsTraining']/option[1]").click()
        self.driver.find_element_by_xpath(".//*[@id='JobplacementsWilliness']/option[1]").click()
        self.driver.find_element_by_xpath(".//*[@type='submit']").click()
        self.driver.find_element_by_xpath(".//*[@class='sldbtnd']/a").click()
        self.driver.implicitly_wait(10)
        self.assertEqual('https://leif.org/commit?product_id=5b304639e59b74063647c484#/',self.driver.current_url )        
        
                
                   
    def test_job_placement_user_senior(self):

        self.driver.get("http://web.linuxjobber.com/users/login")#navigate to linuxjobber.com
        self.driver.implicitly_wait(20)
        username = parser.get('web.linuxjobber.com/users/login', 'username')
        password = parser.get('web.linuxjobber.com/users/login', 'password')
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_xpath(".//*[@type='submit']").click()
        
        self.driver.find_element_by_xpath(".//*[@id='footer-row']/div[2]/ul/li[7]/a").click()
        self.driver.find_element_by_xpath(".//*[@class=' jp2-content']/div/div[2]/div/div/a").click()#Click the Senior Level button
        first_name = parser.get('web.linuxjobber.com/users/login', 'firstname')
        last_name = parser.get('web.linuxjobber.com/users/login', 'lastname')
        email = parser.get('web.linuxjobber.com/users/login', 'email')
        self.driver.find_element_by_id('firstname').send_keys(first_name)
        self.driver.find_element_by_id('lastname').send_keys(last_name)
        self.driver.find_element_by_id('email').send_keys(email)
        self.driver.find_element_by_xpath(".//*[@id='education']/option[5]").click()
        self.driver.find_element_by_id('JobplacementsResume').send_keys("C:\\Users\\Jide\\Desktop\\Training\\Projects\\Linux\\LinuxJobber\\Goals.docx")
        self.driver.find_element_by_xpath(".//*[@id='app']/div[7]/input").click()
                
        self.driver.find_element_by_xpath(".//*[@id='JobplacementsCareer']/option[8]").click()
        self.driver.find_element_by_xpath(".//*[@id='JobplacementsExperience']/option[5]").click()
        self.driver.find_element_by_xpath(".//*[@id='JobplacementsCertification']/option[1]").click()
        self.driver.find_element_by_xpath(".//*[@id='JobplacementsTraining']/option[1]").click()
        self.driver.find_element_by_xpath(".//*[@id='JobplacementsWilliness']/option[1]").click()
        self.driver.find_element_by_xpath(".//*[@type='submit']").click()
        self.driver.find_element_by_xpath(".//*[@class='sldbtnd']/a").click()
        self.driver.implicitly_wait(10)
        self.assertEqual('https://leif.org/commit?product_id=5b304639e59b74063647c484#/',self.driver.current_url )

    def test_job_placement_user_senior_noexperience(self):

        self.driver.get("http://web.linuxjobber.com/users/login")#navigate to linuxjobber.com
        self.driver.implicitly_wait(20)
        username = parser.get('web.linuxjobber.com/users/login', 'username')
        password = parser.get('web.linuxjobber.com/users/login', 'password')
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_xpath(".//*[@type='submit']").click()

        self.driver.find_element_by_xpath(".//*[@id='footer-row']/div[2]/ul/li[7]/a").click()
        self.driver.find_element_by_xpath(".//*[@class=' jp2-content']/div/div[2]/div/div/a").click()#Click the Senior Level button
        first_name = parser.get('web.linuxjobber.com/users/login', 'firstname')
        last_name = parser.get('web.linuxjobber.com/users/login', 'lastname')
        email = parser.get('web.linuxjobber.com/users/login', 'email')
        self.driver.find_element_by_id('firstname').send_keys(first_name)
        self.driver.find_element_by_id('lastname').send_keys(last_name)
        self.driver.find_element_by_id('email').send_keys(email)
        self.driver.find_element_by_xpath(".//*[@id='education']/option[5]").click()
        self.driver.find_element_by_id('JobplacementsResume').send_keys("C:\\Users\\Jide\\Desktop\\Training\\Projects\\Linux\\LinuxJobber\\Goals.docx")
        self.driver.find_element_by_xpath(".//*[@id='app']/div[7]/input").click()
                
        self.driver.find_element_by_xpath(".//*[@id='JobplacementsCareer']/option[8]").click()
        self.driver.find_element_by_xpath(".//*[@id='JobplacementsExperience']/option[1]").click()
        self.driver.find_element_by_xpath(".//*[@id='JobplacementsCertification']/option[1]").click()
        self.driver.find_element_by_xpath(".//*[@id='JobplacementsTraining']/option[1]").click()
        self.driver.find_element_by_xpath(".//*[@id='JobplacementsWilliness']/option[1]").click()
        self.driver.find_element_by_id("but").click()	
        self.assertEqual("http://web.linuxjobber.com/Jobplacements/required", self.driver.current_url)
   


    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()