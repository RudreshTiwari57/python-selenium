from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import unittest
from parameterized import parameterized
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class google(unittest.TestCase):
    def setUp(self):
        print("sample test case started")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.google.com/")
    @parameterized.expand(["javapoint","hello","java"])
    def test_google(self,a):
        self.driver.find_element(By.NAME, "q").send_keys(a)
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.NAME,"btnK")))
        self.driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()
        print("sample test case successfully completed")



