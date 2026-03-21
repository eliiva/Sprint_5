import pytest
import random
import string
from locators import login_and_reg_button
from locators import no_account_button
from locators import input_for_email
from locators import input_for_password
from locators import input_for_repeat_password
from locators import create_account_button
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    yield driver
    driver.quit()

@pytest.fixture()
def valid_email():
    letters = string.ascii_lowercase[:12] 
    email= f"{''.join(random.choice(letters) for i in range(10))}@gmail.com"
    
    return email

@pytest.fixture()
def invalid_email():
    letters = string.ascii_lowercase[:12] 
    email= f"{''.join(random.choice(letters) for i in range(10))}"
    
    return email

@pytest.fixture()
def user(valid_email):
    user = {
        "email": valid_email,
        "password": "123456qW"
        }
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    driver.find_element(By.XPATH, login_and_reg_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, no_account_button)))
    driver.find_element(By.XPATH, no_account_button).click()
    driver.find_element(By.XPATH, input_for_email).send_keys(user['email'])
    driver.find_element(By.XPATH, input_for_password).send_keys(user['password'])
    driver.find_element(By.XPATH, input_for_repeat_password).send_keys(user['password'])
    driver.find_element(By.XPATH, create_account_button).click()

    driver.quit()
    
    return user
