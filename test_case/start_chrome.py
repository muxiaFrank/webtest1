#coding=utf-8
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import unittest, time, re

import sys
sys.path.append("\public")

from public import login


class RDMchrome(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver

        cls.driver = webdriver.Chrome(chromedriver)

        cls.driver.implicitly_wait(30)
        cls.base_url = "http://192.168.1.18:2000/"
        cls.verificationErrors = []
        cls.accept_next_alert = True


    def setUp(self):
        print "setup"

    def tearDown(self):
        print 'teardown'

    def test_1login(self):
        """登录RDM"""

        driver = self.driver
        driver.get(self.base_url + "/")

        login.login(self)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()