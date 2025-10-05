from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants.auth import AUTH_TEST_EMAIL, AUTH_TEST_PASSWORD, TEST_EMAIL, TEST_PASSWORD
from helpers import go_to_login_page, fill_login_form
from locators import *


class TestProfile:
    def login(self, driver, email, password):
        go_to_login_page(driver, way="main")

        fill_login_form(driver, email, password)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(HEADER_PROFILE_BUTTON))

    def test_go_to_profile(self, browser):
        self.login(browser, TEST_EMAIL, TEST_PASSWORD)

        browser.find_element(*HEADER_PROFILE_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(PROFILE_SECTION))

        assert browser.find_element(*PROFILE_SECTION).is_displayed()

    def test_logout(self, browser):
        self.login(browser, AUTH_TEST_EMAIL, AUTH_TEST_PASSWORD)

        browser.find_element(*HEADER_PROFILE_BUTTON).click()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(PROFILE_LOGOUT_BUTTON))

        browser.find_element(*PROFILE_LOGOUT_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(LOGIN_SUBMIT_BUTTON))

        assert browser.find_element(*LOGIN_SUBMIT_BUTTON).is_displayed()
