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

class UserInterestPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()

    def test_userinterestpage(self):
        self.driver.get('http://34.221.68.130:4000/courses/userinterest')
        #Click the linux fundamentals course in the user Interest Courses to see the description page
        self.driver.find_element_by_id('box-color').click()
        self.driver.implicitly_wait(10)
        course_topic_title = self.driver.find_element_by_class_name("course-intro-title")
        #Print the title of the course description in console
        print (course_topic_title.text) 
        #Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('Linux Fundamentals', course_topic_title.text)
        #go back on the driver and test other course links
        self.driver.back()
        time.sleep(2)
        #Click the linux proficiency course description
        self.driver.find_element_by_id('box-color2').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        #Print the title of the course description in console
        print (course_topic_title)
        #Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('Linux Proficiency', course_topic_title)
        #go back on the driver and test other course links
        self.driver.back()
        time.sleep(2)
        #Click the HTML & CSS course description
        self.driver.find_element_by_id('box-color3').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        #Print the title of the course description in console
        print (course_topic_title)
        #Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('HTML & CSS', course_topic_title)
        #go back on the driver and test other course links
        self.driver.back()
        time.sleep(2)
        #Click the AWS proficiency course description
        self.driver.find_element_by_id('box-color4').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        #Print the title of the course description in console
        print (course_topic_title)
        #Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('AWS', course_topic_title)
        #go back on the driver and test other course links
        self.driver.back()
        time.sleep(2)
        #Click the Puppet Training proficiency course description
        self.driver.find_element_by_id('box-color5').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        #Print the title of the course description in console
        print (course_topic_title)
        #Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('Puppet Training', course_topic_title)
        #go back on the driver and test other course links
        self.driver.back()
        time.sleep(2)
        #Click the JAVA proficiency course description
        self.driver.find_element_by_id('box-color6').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        #Print the title of the course description in console
        print (course_topic_title)
        #Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('JAVA', course_topic_title)
        #go back on the driver and test other course links
        self.driver.back()
        time.sleep(2)
        #Click the RHCSA proficiency course description
        self.driver.find_element_by_id('box-color7').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        #Print the title of the course description in console
        print (course_topic_title)
        #Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('RHCSA', course_topic_title)
        #go back on the driver and test other course links
        self.driver.back()
        time.sleep(2)
        #Click the Angular course description
        self.driver.find_element_by_id('box-color8').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        #Print the title of the course description in console
        print (course_topic_title)
        #Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('Angular', course_topic_title)
        #go back on the driver and test other course links
        self.driver.back()
        time.sleep(2)
        #Click the Cyber Security course description
        self.driver.find_element_by_id('box-color9').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        #Print the title of the course description in console
        print (course_topic_title)
        #Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('Cyber Security', course_topic_title)
        #go back on the driver and test other course links
        self.driver.back()
        time.sleep(2)
        #Click the business Analysis course description
        self.driver.find_element_by_id('box-color10').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        #Print the title of the course description in console
        print (course_topic_title)
        #Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('Business Analysis', course_topic_title)
        #go back on the driver and test other course links
        self.driver.back()
        time.sleep(2)
        #Click the  course description
        self.driver.find_element_by_id('box-color11').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        #Print the title of the course description in console
        print (course_topic_title)
        #Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('Linux Proficiency', course_topic_title)
        #go back on the driver and test other course links
        self.driver.back()
        time.sleep(2)
        #Click the Database course description
        self.driver.find_element_by_id('box-color12').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        #Print the title of the course description in console
        print (course_topic_title)
        #Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('Database', course_topic_title)
        #go back on the driver and test other course links
        self.driver.back()
        time.sleep(2)
        #Click the Python course description
        self.driver.find_element_by_id('box-color13').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        #Print the title of the course description in console
        print (course_topic_title)
        #Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('Python', course_topic_title)



    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()