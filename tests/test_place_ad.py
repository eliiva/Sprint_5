import pytest
from locators import login_and_reg_button, input_for_email, input_for_password, place_ad_button, modal_header, login_button, goods_name_input, goods_description_textarea, goods_price_input, dropdown_list_buttons, books_category_button, city_category_button, radiobuttons_list, place_ad_submit_button, user_avatar, placed_ad_name
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_failed_place_ad_logout_user_popup_with_text(driver):
    driver.find_element(By.XPATH, place_ad_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, modal_header)))

    assert driver.find_element(By.XPATH, modal_header).text == "Чтобы разместить объявление, авторизуйтесь"

def test_place_ad_login_user_ad_successfully_placed(driver, user):
    driver.find_element(By.XPATH, login_and_reg_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, login_button)))
    driver.find_element(By.XPATH, input_for_email).send_keys(user['email'])
    driver.find_element(By.XPATH, input_for_password).send_keys(user['password'])
    driver.find_element(By.XPATH, login_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element((By.XPATH, login_and_reg_button)))
    driver.find_element(By.XPATH, place_ad_button).click()
    driver.find_element(By.XPATH, goods_name_input).send_keys("Идиот")
    driver.find_element(By.XPATH, goods_description_textarea).send_keys("роман")
    driver.find_element(By.XPATH, goods_price_input).send_keys(350)
    dropdown_category_button = driver.find_elements(By.XPATH, dropdown_list_buttons)[0]
    dropdown_category_button.click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, books_category_button)))
    driver.find_element(By.XPATH, books_category_button).click()
    dropdown_city_button = driver.find_elements(By.XPATH, dropdown_list_buttons)[1]
    dropdown_city_button.click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, city_category_button)))
    driver.find_element(By.XPATH, city_category_button).click()
    driver.find_elements(By.XPATH, radiobuttons_list)[1].click()
    driver.find_element(By.XPATH, place_ad_submit_button).click()
    driver.refresh()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, user_avatar)))
    driver.find_element(By.XPATH, user_avatar).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, placed_ad_name)))

    assert driver.find_element(By.XPATH, placed_ad_name).text == "Идиот"
