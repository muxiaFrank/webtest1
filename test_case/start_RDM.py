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
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.18:2000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        """登录RDM"""

        driver = self.driver
        driver.get(self.base_url + "/")

        login.login(self)


    def tearDown(self):
        self.driver.quit()

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()