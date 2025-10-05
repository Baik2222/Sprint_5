from locators import *


def fill_registration_form(driver, name, email, password):
    driver.find_element(*REGISTER_NAME_INPUT).send_keys(name)
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(email)
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*REGISTER_SUBMIT_BUTTON).click()


def fill_login_form(driver, email, password):
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()


def get_error_message(driver):
    return driver.find_element(*REGISTER_ERROR_MESSAGE).text
