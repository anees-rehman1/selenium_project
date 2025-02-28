import time
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def setup_function():
    global driver
    service=Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    # options = webdriver.ChromeOptions()

    time.sleep(2)
    driver.maximize_window()
    time.sleep(3)
    driver.get("https://urducourses.pk/tutor-login-2/")
    time.sleep(3)

def my_cred():
    return [
        ("anessurrehman6@gmail.com", "urducourses@1234"),
        ("ali@gmil.com", "ali@123"),
        ("new@gmil.com", "ok@123")
    ]

def teardown_function():
    driver.quit()

@pytest.mark.parametrize("username,password",my_cred())
def test_login(username,password):
    print("mypytest login1 ...")
    driver.find_element(By.XPATH,'//*[@id="tutor-login-form"]/div[1]/input').send_keys(username)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="tutor-login-form"]/div[2]/input').send_keys(password)
    time.sleep(1)
    allure.attach(driver.get_full_page_screenshot_as_png(),name="myalnafi_sc",attachment_type=AttachmentType.PNG)
