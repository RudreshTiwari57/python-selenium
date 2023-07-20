from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import unittest
from parameterized import parameterized
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class dropdown(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.wikipedia.org/")
    def test_dropdown(self):
        dropdown = self.driver.find_element(By.ID,"searchLanguage")
        time.sleep(1)
        select = Select(dropdown)
        select.select_by_visible_text("Afrikaans")
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

