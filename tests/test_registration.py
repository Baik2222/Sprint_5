import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants.site import BASE_URL
from locators import *
from constants.utils import generate_email, generate_password


def go_to_registration_page(driver):
    driver.get(BASE_URL)
    driver.find_element(*MAIN_LOGIN_BUTTON).click()
    driver.find_element(*REGISTER_PAGE_LINK).click()


def fill_registration_form(driver, name, email, password):
    driver.find_element(*REGISTER_NAME_INPUT).send_keys(name)
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(email)
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*REGISTER_SUBMIT_BUTTON).click()


def get_error_message(driver):
    return driver.find_element(*REGISTER_ERROR_MESSAGE).text


def test_success_registration(browser):
    go_to_registration_page(browser)

    fill_registration_form(browser, "Тест", generate_email(), generate_password())
    WebDriverWait(browser, 5).until(EC.presence_of_element_located(LOGIN_SUBMIT_BUTTON))

    assert browser.find_element(*LOGIN_SUBMIT_BUTTON)


@pytest.mark.parametrize("password", ["12345", "abcde", " "])
def test_registration_with_invalid_password(browser, password):
    go_to_registration_page(browser)

    fill_registration_form(browser, "Тест", generate_email(), password)
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(REGISTER_ERROR_MESSAGE))

    error = get_error_message(browser)

    assert "пароль" in error.lower()
