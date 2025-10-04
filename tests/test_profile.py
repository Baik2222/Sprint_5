from locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants.site import BASE_URL
from constants.auth import TEST_EMAIL, TEST_PASSWORD


def login(driver, email, password):
    driver.get(BASE_URL)

    driver.find_element(*MAIN_LOGIN_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)

    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(HEADER_PROFILE_BUTTON))



def test_go_to_profile(browser):
    login(browser, TEST_EMAIL, TEST_PASSWORD)

    browser.find_element(*HEADER_PROFILE_BUTTON).click()
    WebDriverWait(browser, 5).until(EC.presence_of_element_located(PROFILE_SECTION))

    assert browser.find_element(*PROFILE_SECTION)


def test_logout(browser):
    browser.get(BASE_URL)
    exists_test_mail = "mymail@yandex.ru"
    exists_test_password = "Strong123"

    browser.find_element(*HEADER_PROFILE_BUTTON).click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(LOGIN_EMAIL_INPUT))

    browser.find_element(*LOGIN_EMAIL_INPUT).send_keys(exists_test_mail)
    browser.find_element(*LOGIN_PASSWORD_INPUT).send_keys(exists_test_password)
    browser.find_element(*LOGIN_SUBMIT_BUTTON).click()
    WebDriverWait(browser, 5).until(EC.presence_of_element_located(HEADER_PROFILE_BUTTON))

    browser.find_element(*HEADER_PROFILE_BUTTON).click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(PROFILE_LOGOUT_BUTTON))

    browser.find_element(*PROFILE_LOGOUT_BUTTON).click()
    WebDriverWait(browser, 5).until(EC.presence_of_element_located(LOGIN_SUBMIT_BUTTON))

    assert "login" in browser.current_url or browser.find_element(*LOGIN_SUBMIT_BUTTON)
