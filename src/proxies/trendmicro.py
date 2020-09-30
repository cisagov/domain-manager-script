# mypy: ignore-errors
# flake8: noqa
# Generated by Selenium IDE
# Standard Python Libraries
import json
import os
import sys
import time

# Third-Party Libraries
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from twocaptcha import TwoCaptcha


def get_and_solve(url):

    recaptcha_element = driver.find_element(By.CLASS_NAME, "g-recaptcha")
    sitekey = recaptcha_element.get_attribute("data-sitekey")
    print(sitekey)

    solver = TwoCaptcha(api_key)
    try:
        result = solver.recaptcha(sitekey=sitekey, url=url)

    except Exception as e:
        print(e)
    else:
        driver.execute_script(
            "document.getElementById('g-recaptcha-response').innerHTML='"
            + result["code"]
            + "';"
        )
        time.sleep(3)


driver.get("https://global.sitesafety.trendmicro.com/")
driver.set_window_size(2576, 1416)
driver.find_element(By.ID, "urlname").click()
driver.find_element(By.ID, "urlname").click()
driver.find_element(By.ID, "urlname").send_keys(f"http://{domain}")
driver.find_element(By.ID, "getinfo").click()
driver.find_element(By.ID, "myBtn").click()
driver.find_element(By.CSS_SELECTOR, ".modal_content_2:nth-child(2) a").click()
driver.find_element(By.CSS_SELECTOR, ".lightbg:nth-child(4) input").click()
driver.find_element(By.CSS_SELECTOR, ".suggestoption > .radioinput").click()
driver.find_element(By.ID, "radio5").click()
driver.find_element(By.CSS_SELECTOR, ".General .normal").click()
driver.find_element(By.CSS_SELECTOR, ".Business .normal").click()
time.sleep(1)
driver.find_element(
    By.CSS_SELECTOR, "#Business .child_row_01:nth-child(3) .radio_c1"
).click()
driver.find_element(By.ID, "owner").click()
driver.find_element(By.ID, "comments").click()
driver.find_element(By.ID, "comments").send_keys("Changing Website for customer")
driver.find_element(By.ID, "textfieldemail").send_keys("barry.k.hansen@gmail.com")
get_and_solve("https://global.sitesafety.trendmicro.com/")
driver.find_element(By.NAME, "send").click()
driver.find_element(By.LINK_TEXT, "Check a URL").click()
