import time

from selenium import webdriver
import unittest
from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By


# we pass TestCase in the class to run the unittest
class Openbrowser(unittest.TestCase):

    #the setUp method is the first method to run will runing a test case
    #there should always a setup method in the class
    def setUp(self):
        #creating the object of the chrome class
        self.driver = Chrome()
        self.driver.get("https://www.google.com/")
    #the test definition name should always start with the "test_" then followed by the name of the test

    def test_google(self):
        self.driver.find_element(By.NAME, "q").send_keys("a")
        #Implicit Wait directs the Selenium WebDriver to wait for a certain measure of time before throwing an exception
        #it is the method of the browser class
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)
        self.driver.implicitly_wait(5)
    # this is the last method that will run after each test definition
    def tearDown(self):

        self.driver.quit()