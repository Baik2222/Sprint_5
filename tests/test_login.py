import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants.auth import TEST_EMAIL, TEST_PASSWORD
from helpers import go_to_login_page, fill_login_form
from locators import *


class TestLogin:
    @pytest.mark.parametrize("way", ["main", "profile", "registration"])
    def test_login_various_ways(self, browser, way):
        go_to_login_page(browser, way)

        fill_login_form(browser, TEST_EMAIL, TEST_PASSWORD)
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(HEADER_PROFILE_BUTTON))

        assert browser.find_element(*HEADER_PROFILE_BUTTON).is_displayed()
