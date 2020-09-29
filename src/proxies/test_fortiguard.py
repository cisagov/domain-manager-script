# mypy: ignore-errors
# flake8: noqa
# Generated by Selenium IDE
# Standard Python Libraries
import json
import os
import time

# Third-Party Libraries
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestFortiguard:
    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path="./drivers/chromedriver")
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_fortiguard(self):
        self.driver.get("https://www.fortiguard.com/faq/wfratingsubmit")
        self.driver.set_window_size(1680, 979)
        self.driver.find_element(By.ID, "__agreementButton").click()
        self.driver.find_element(By.ID, "web_filter_rating_info_form_url").click()
        self.driver.find_element(By.ID, "web_filter_rating_info_form_url").click()
        self.driver.find_element(By.ID, "web_filter_rating_info_form_url").send_keys(
            "https://www.northwestaustindentists.com/"
        )
        self.driver.find_element(
            By.ID, "web_filter_rating_info_form_categorysuggestion"
        ).click()
        dropdown = self.driver.find_element(
            By.ID, "web_filter_rating_info_form_categorysuggestion"
        )
        dropdown.find_element(By.XPATH, "//option[. = 'Health and Wellness']").click()
        self.driver.find_element(
            By.CSS_SELECTOR, ".page-section > .row:nth-child(2)"
        ).click()
        self.driver.find_element(By.ID, "web_filter_rating_info_form_name").click()
        self.driver.find_element(By.ID, "web_filter_rating_info_form_name").send_keys(
            "Mostafa Abdo"
        )
        self.driver.find_element(By.ID, "web_filter_rating_info_form_email").send_keys(
            "mostafaxcali@gmail.com"
        )
        self.driver.find_element(
            By.ID, "web_filter_rating_info_form_companyname"
        ).send_keys("INL")
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_xpath('//iframe[contains(@src, "recaptcha")]')
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, "web_filter_rating_info_form_submit").click()


fortiguard = TestFortiguard()
fortiguard.setup_method()
fortiguard.test_fortiguard()
