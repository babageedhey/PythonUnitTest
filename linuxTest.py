import unittest
import time
import HTMLTestRunner
import os
import userTest
import groupClassTest
import resumeTest
import studentPackageTest
import accountSettingTest
import jobPlacementTest

direct = os.getcwd()

from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



class MyTestSuite(unittest.TestCase):
    def test_allTest(self):
        linux_Test = unittest.TestSuite()
        linux_Test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(userTest.UserTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(groupClassTest.GroupTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(resumeTest.ResumeTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(studentPackageTest.StudPackageTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(accountSettingTest.AccountSettingTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(jobPlacementTest.JobPlacementTest),
        ])

        outfield = open(direct + "\LinuxTest.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream= outfield,
            title= "LinuxJobber Test Report",
            description= "An Automated Test for the Components on the Web Page"
        )

        runner1.run(linux_Test)


if __name__ == '__main__':
    unittest.main()
