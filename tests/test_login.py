import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

from constants.site import BASE_URL
from constants.auth import TEST_EMAIL, TEST_PASSWORD


def go_to_login_page(driver, way="main"):
    driver.get(BASE_URL)

    if way == "main":
        driver.find_element(*MAIN_LOGIN_BUTTON).click()
    elif way == "profile":
        driver.find_element(*HEADER_PROFILE_BUTTON).click()
    elif way == "registration":
        driver.find_element(*MAIN_LOGIN_BUTTON).click()
        driver.find_element(*REGISTER_PAGE_LINK).click()
        driver.find_element(*LOGIN_LINK_ON_REGISTER_PAGE).click()


def fill_login_form(driver, email, password):
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()


@pytest.mark.parametrize("way", ["main", "profile", "registration"])
def test_login_various_ways(browser, way):
    go_to_login_page(browser, way)

    fill_login_form(browser, TEST_EMAIL, TEST_PASSWORD)
    WebDriverWait(browser, 5).until(EC.presence_of_element_located(HEADER_PROFILE_BUTTON))

    assert browser.find_element(*HEADER_PROFILE_BUTTON)
