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

class FooterLinkTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()

    def test_footer_home(self):
        self.driver.get('http://54.149.10.37:8005')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Home').click()
        time.sleep(2)
        self.assertEqual('http://54.149.10.37:8005/', self.driver.current_url)

    def test_footer_AboutUS(self):
        self.driver.get('http://54.149.10.37:8005')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('About US').click()
        time.sleep(2)
        self.assertEqual('http://54.149.10.37:8005/aboutus', self.driver.current_url)

    def test_footer_Resume_Services(self):
        self.driver.get('http://54.149.10.37:8005')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Resume Services').click()
        self.assertEqual('http://54.149.10.37:8005/resumeservice', self.driver.current_url)

    def test_footer_Student_Packages(self):
        self.driver.get('http://54.149.10.37:8005')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Student Packages').click()
        self.assertEqual('http://54.149.10.37:8005/home/packages', self.driver.current_url)

    def test_footer_Servcer_Services(self):
        self.driver.get('http://54.149.10.37:8005')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Server Services').click()
        self.assertEqual('http://54.149.10.37:8005/home/server/service', self.driver.current_url)

    def test_footer_Live_Help(self):
        self.driver.get('http://54.149.10.37:8005')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Live Help').click()
        self.assertEqual('http://54.149.10.37:8005/home/livehelp', self.driver.current_url)

    def test_footer_Projects(self):
        self.driver.get('http://54.149.10.37:8005')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Projects').click()
        self.assertEqual('http://54.149.10.37:8005/projects/', self.driver.current_url)

    def test_footer_faq(self):
        self.driver.get('http://54.149.10.37:8005')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('FAQ').click()
        self.assertEqual('http://54.149.10.37:8005/faq', self.driver.current_url)

    def test_footer_Contact(self):
        self.driver.get('http://54.149.10.37:8005')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Contact Us').click()
        self.assertEqual('http://54.149.10.37:8005/companys/contact', self.driver.current_url)

    def test_footer_GroupClass(self):
        self.driver.get('http://54.149.10.37:8005')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Group Class').click()
        self.assertEqual('http://54.149.10.37:8005/groupCourse', self.driver.current_url)

    def test_footer_InPerson(self):
        self.driver.get('http://54.149.10.37:8005')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('In-Person Training').click()
        self.assertEqual('http://54.149.10.37:8005/home/liveinstructor', self.driver.current_url)

    def test_footer_WorkExperience(self):
        self.driver.get('http://54.149.10.37:8005')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Work Experience').click()
        self.assertEqual('http://54.149.10.37:8005/workexperience/', self.driver.current_url)

    def test_footer_Gain_Experience(self):
        self.driver.get('http://54.149.10.37:8005')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Gain Experience').click()
        self.assertEqual('http://54.149.10.37:8005/gainexperience', self.driver.current_url)

    def test_footer_Job_Placement(self):
        self.driver.get('http://54.149.10.37:8005')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Job Placement Program').click()
        self.assertEqual('http://54.149.10.37:8005/jobplacements/', self.driver.current_url)


    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()