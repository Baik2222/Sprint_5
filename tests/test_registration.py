import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants.utils import generate_email, generate_password
from helpers import go_to_registration_page, fill_registration_form, get_error_message
from locators import *


class TestRegistration:
    def test_success_registration(self, browser):
        go_to_registration_page(browser)

        fill_registration_form(browser, "Тест", generate_email(), generate_password())
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(LOGIN_SUBMIT_BUTTON))

        assert browser.find_element(*LOGIN_SUBMIT_BUTTON).is_displayed()

    @pytest.mark.parametrize("password", ["12345", "abcde", " "])
    def test_registration_with_invalid_password(self, browser, password):
        go_to_registration_page(browser)

        fill_registration_form(browser, "Тест", generate_email(), password)
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(REGISTER_ERROR_MESSAGE))

        error = get_error_message(browser)

        assert "пароль" in error.lower()
