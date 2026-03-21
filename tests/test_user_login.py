import pytest
from locators import login_and_reg_button
from locators import input_for_email
from locators import input_for_password
from locators import user_name
from locators import user_avatar
from locators import login_button
from locators import logout_button
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_login_exist_user_page_has_user_name(driver, user):
    driver.find_element(By.XPATH, login_and_reg_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, login_button)))
    driver.find_element(By.XPATH, input_for_email).send_keys(user['email'])
    driver.find_element(By.XPATH, input_for_password).send_keys(user['password'])
    driver.find_element(By.XPATH, login_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element((By.XPATH, login_and_reg_button)))

    assert driver.find_element(By.XPATH, user_name)

def test_login_exist_user_page_has_user_avatar(driver, user):
    driver.find_element(By.XPATH, login_and_reg_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, login_button)))
    driver.find_element(By.XPATH, input_for_email).send_keys(user['email'])
    driver.find_element(By.XPATH, input_for_password).send_keys(user['password'])
    driver.find_element(By.XPATH, login_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element((By.XPATH, login_and_reg_button)))

    assert driver.find_element(By.XPATH, user_avatar)

def test_logout_exist_user_page_reg_button_visible(driver, user):
    driver.find_element(By.XPATH, login_and_reg_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, login_button)))
    driver.find_element(By.XPATH, input_for_email).send_keys(user['email'])
    driver.find_element(By.XPATH, input_for_password).send_keys(user['password'])
    driver.find_element(By.XPATH, login_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element((By.XPATH, login_and_reg_button)))
    driver.find_element(By.XPATH, logout_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element((By.XPATH, logout_button)))

    assert driver.find_element(By.XPATH, login_and_reg_button)

def test_logout_exist_user_page_has_not_user_name(driver, user):
    driver.find_element(By.XPATH, login_and_reg_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, login_button)))
    driver.find_element(By.XPATH, input_for_email).send_keys(user['email'])
    driver.find_element(By.XPATH, input_for_password).send_keys(user['password'])
    driver.find_element(By.XPATH, login_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element((By.XPATH, login_and_reg_button)))
    driver.find_element(By.XPATH, logout_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element((By.XPATH, logout_button)))

    assert len(driver.find_elements(By.XPATH, user_name)) == 0

def test_logout_exist_user_page_has_not_user_avatar(driver, user):
    driver.find_element(By.XPATH, login_and_reg_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, login_button)))
    driver.find_element(By.XPATH, input_for_email).send_keys(user['email'])
    driver.find_element(By.XPATH, input_for_password).send_keys(user['password'])
    driver.find_element(By.XPATH, login_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element((By.XPATH, login_and_reg_button)))
    driver.find_element(By.XPATH, logout_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element((By.XPATH, logout_button)))

    assert len(driver.find_elements(By.XPATH, user_avatar)) == 0
    