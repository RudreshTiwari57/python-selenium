import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

import unittest
from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Explicit_Wait(unittest.TestCase):

    # the setUp method is the first method to run will runing a test case
    # there should always a setup method in the class
    def setUp(self):
        # creating the object of the chrome class
        self.driver = Chrome()
        self.driver.get("https://www.google.com/")

    # the test definition name should always start with the "test_" then followed by the name of the test

    def test_google(self):
        self.driver.find_element(By.NAME, "q").send_keys("a")
        # Explicit Wait command, the WebDriver is directed to wait until a certain condition occurs before proceeding with executing the code.
        # it is the method of the browser class
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.NAME,"btnK")))
        self.driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.NAME,"btnK")))

    # this is the last method that will run after each test definition
    def tearDown(self):
        self.driver.quit()



