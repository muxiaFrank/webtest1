# coding = utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time


def login(self):

    self.driver.find_element_by_id("userName").clear
    self.driver.find_element_by_id("userName").send_keys("yangwl")

    self.driver.find_element_by_id("userPassword").clear
    self.driver.find_element_by_id("userPassword").send_keys("qwer.123")

    self.driver.find_element_by_id("loginBtn").click()


    time.sleep(2)
