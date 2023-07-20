# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDirectory():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_directory(self):
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    self.driver.set_window_size(1056, 608)
    self.driver.find_element(By.LINK_TEXT, "Directory").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input").send_keys("Odis  Adalwin")
    element = self.driver.find_element(By.CSS_SELECTOR, ".oxd-grid-3 > .oxd-grid-item:nth-child(1)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
  