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

class TestPimaddemployee():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_pimaddemployee(self):
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    self.driver.set_window_size(1056, 608)
    self.driver.find_element(By.LINK_TEXT, "PIM").click()
    element = self.driver.find_element(By.LINK_TEXT, "Add Employee")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "Add Employee").click()
    self.driver.find_element(By.NAME, "firstName").click()
    self.driver.find_element(By.NAME, "firstName").send_keys("aaa")
    self.driver.find_element(By.NAME, "middleName").click()
    self.driver.find_element(By.NAME, "middleName").send_keys("bbb")
    self.driver.find_element(By.NAME, "lastName").click()
    self.driver.find_element(By.NAME, "lastName").send_keys("ccc")
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-switch-input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").send_keys("aaabbbccc")
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").send_keys("aaabbbccc")
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").send_keys("aaabbbccc")
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input-group:nth-child(2) .oxd-radio-wrapper > label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input-group:nth-child(1) > div > .oxd-radio-wrapper > label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").send_keys("aaabbbccc1")
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").send_keys("aaabbbccc1")
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").send_keys("aaabbbccc123")
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").send_keys("aaabbbccc123")
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--secondary").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--secondary")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".orangehrm-background-container").click()
  
