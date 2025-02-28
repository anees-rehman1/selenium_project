import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def setup_function():
    global driver
    service=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    # options = webdriver.ChromeOptions()
    time.sleep(2)
    driver.maximize_window()
    time.sleep(3)
    driver.get("https://urducourses.pk/tutor-login-2/")
    time.sleep(3)

def teardown_function():
    driver.quit()

@pytest.mark.parametrize("username,password",[("anessurrehman6@gmail.com","urducourses@1234")])
def test_login(username,password):
    print("mypytest login1 ...")
    driver.find_element(By.XPATH,'//*[@id="tutor-login-form"]/div[1]/input').send_keys(username)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="tutor-login-form"]/div[2]/input').send_keys(password)
    time.sleep(2)
