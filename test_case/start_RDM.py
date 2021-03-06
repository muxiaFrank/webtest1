#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner #引入HTMLTestRunner 包
from selenium.webdriver.common.action_chains import ActionChains
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import sys
sys.path.append("\public")
#导入登录、退出模块
from public import login


class RDM(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
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

    def test_2login(self):
        """登录RDM"""

        driver = self.driver
        driver.get(self.base_url + "/")

        login.login(self)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()