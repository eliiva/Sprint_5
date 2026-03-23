import pytest
from locators import login_and_reg_button, no_account_button, input_for_email, input_for_password, input_for_repeat_password, create_account_button, user_name, user_avatar, error_message, div_for_email_input, div_for_password_input, div_for_repeat_password_input
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_registration_valid_data_redirect_rto_main_page(driver, valid_email):
    password = "123456qW"

    driver.find_element(By.XPATH, login_and_reg_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, no_account_button)))
    driver.find_element(By.XPATH, no_account_button).click()
    driver.find_element(By.XPATH, input_for_email).send_keys(valid_email)
    driver.find_element(By.XPATH, input_for_password).send_keys(password)
    driver.find_element(By.XPATH, input_for_repeat_password).send_keys(password)
    driver.find_element(By.XPATH, create_account_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element((By.XPATH, login_and_reg_button)))

    assert "/regiatration" in driver.current_url

def test_registration_valid_data_page_has_user_name(driver, valid_email):
    password = "123456qW"

    driver.find_element(By.XPATH, login_and_reg_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, no_account_button)))
    driver.find_element(By.XPATH, no_account_button).click()
    driver.find_element(By.XPATH, input_for_email).send_keys(valid_email)
    driver.find_element(By.XPATH, input_for_password).send_keys(password)
    driver.find_element(By.XPATH, input_for_repeat_password).send_keys(password)
    driver.find_element(By.XPATH, create_account_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element((By.XPATH, login_and_reg_button)))

    assert driver.find_element(By.XPATH, user_name)

def test_registration_valid_data_page_has_user_avatar(driver, valid_email):
    password = "123456qW"

    driver.find_element(By.XPATH, login_and_reg_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, no_account_button)))
    driver.find_element(By.XPATH, no_account_button).click()
    driver.find_element(By.XPATH, input_for_email).send_keys(valid_email)
    driver.find_element(By.XPATH, input_for_password).send_keys(password)
    driver.find_element(By.XPATH, input_for_repeat_password).send_keys(password)
    driver.find_element(By.XPATH, create_account_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element((By.XPATH, login_and_reg_button)))

    assert driver.find_element(By.XPATH, user_avatar)

def test_registration_invalid_email_alert(driver, invalid_email):
    driver.find_element(By.XPATH, login_and_reg_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, no_account_button)))
    driver.find_element(By.XPATH, no_account_button).click()
    driver.find_element(By.XPATH, input_for_email).send_keys(invalid_email)
    driver.find_element(By.XPATH, create_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, error_message)))

    assert driver.find_element(By.XPATH, error_message).text == "Ошибка"

def test_registration_invalid_email_red_border_email_input(driver, invalid_email):
    driver.find_element(By.XPATH, login_and_reg_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, no_account_button)))
    driver.find_element(By.XPATH, no_account_button).click()
    driver.find_element(By.XPATH, input_for_email).send_keys(invalid_email)
    driver.find_element(By.XPATH, create_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, error_message)))

    assert driver.find_element(By.XPATH, div_for_email_input).get_attribute("class") == "input_inputError__fLUP9"

def test_registration_invalid_email_red_border_password_input(driver, invalid_email):
    driver.find_element(By.XPATH, login_and_reg_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, no_account_button)))
    driver.find_element(By.XPATH, no_account_button).click()
    driver.find_element(By.XPATH, input_for_email).send_keys(invalid_email)
    driver.find_element(By.XPATH, create_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, error_message)))

    assert driver.find_element(By.XPATH, div_for_password_input).get_attribute("class") == "input_inputError__fLUP9"

def test_registration_invalid_email_red_border_password_repeat_input(driver, invalid_email):
    driver.find_element(By.XPATH, login_and_reg_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, no_account_button)))
    driver.find_element(By.XPATH, no_account_button).click()
    driver.find_element(By.XPATH, input_for_email).send_keys(invalid_email)
    driver.find_element(By.XPATH, create_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, error_message)))

    assert driver.find_element(By.XPATH, div_for_repeat_password_input).get_attribute("class") == "input_inputError__fLUP9"

def test_registration_exist_email_alert(driver, user):
    driver.find_element(By.XPATH, login_and_reg_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, no_account_button)))
    driver.find_element(By.XPATH, no_account_button).click()
    driver.find_element(By.XPATH, input_for_email).send_keys(user['email'])
    driver.find_element(By.XPATH, input_for_password).send_keys(user['password'])
    driver.find_element(By.XPATH, input_for_repeat_password).send_keys(user['password'])
    driver.find_element(By.XPATH, create_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, error_message)))

    assert driver.find_element(By.XPATH, error_message).text == "Ошибка"

def test_registration_exist_email_red_border_email_input(driver, user):
    driver.find_element(By.XPATH, login_and_reg_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, no_account_button)))
    driver.find_element(By.XPATH, no_account_button).click()
    driver.find_element(By.XPATH, input_for_email).send_keys(user['email'])
    driver.find_element(By.XPATH, input_for_password).send_keys(user['password'])
    driver.find_element(By.XPATH, input_for_repeat_password).send_keys(user['password'])
    driver.find_element(By.XPATH, create_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, error_message)))

    assert driver.find_element(By.XPATH, div_for_email_input).get_attribute("class") == "input_inputError__fLUP9"

def test_registration_exist_email_red_border_password_input(driver, user):
    driver.find_element(By.XPATH, login_and_reg_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, no_account_button)))
    driver.find_element(By.XPATH, no_account_button).click()
    driver.find_element(By.XPATH, input_for_email).send_keys(user['email'])
    driver.find_element(By.XPATH, input_for_password).send_keys(user['password'])
    driver.find_element(By.XPATH, input_for_repeat_password).send_keys(user['password'])
    driver.find_element(By.XPATH, create_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, error_message)))

    assert driver.find_element(By.XPATH, div_for_password_input).get_attribute("class") == "input_inputError__fLUP9"

def test_registration_exist_email_red_border_repeat_password_input(driver, user):
    driver.find_element(By.XPATH, login_and_reg_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, no_account_button)))
    driver.find_element(By.XPATH, no_account_button).click()
    driver.find_element(By.XPATH, input_for_email).send_keys(user['email'])
    driver.find_element(By.XPATH, input_for_password).send_keys(user['password'])
    driver.find_element(By.XPATH, input_for_repeat_password).send_keys(user['password'])
    driver.find_element(By.XPATH, create_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, error_message)))

    assert driver.find_element(By.XPATH, div_for_repeat_password_input).get_attribute("class") == "input_inputError__fLUP9"
