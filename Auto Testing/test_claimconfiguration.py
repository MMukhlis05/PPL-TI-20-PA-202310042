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

class TestClaimconfiguration():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_claimconfiguration(self):
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    self.driver.set_window_size(1056, 608)
    self.driver.find_element(By.LINK_TEXT, "Claim").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\--parent > .oxd-topbar-body-nav-tab-item").click()
    self.driver.find_element(By.LINK_TEXT, "Events").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input").send_keys("Accommodation")
    element = self.driver.find_element(By.CSS_SELECTOR, ".oxd-form")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-textarea").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-switch-input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-switch-input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--secondary").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-table-card:nth-child(1) .oxd-icon-button:nth-child(1) > .oxd-icon").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".oxd-table-card:nth-child(1) .oxd-icon-button:nth-child(1) > .oxd-icon")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--text").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\--parent > .oxd-topbar-body-nav-tab-item").click()
    self.driver.find_element(By.LINK_TEXT, "Expense Types").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input").send_keys("Accommodation")
    element = self.driver.find_element(By.CSS_SELECTOR, ".oxd-form-actions")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--ghost").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-table-card:nth-child(1) .oxd-icon-button:nth-child(1) > .oxd-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--text").click()
  