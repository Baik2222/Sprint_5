import pytest
from locators import *
from constants.site import BASE_URL


class TestConstructorTabs:
    @pytest.mark.parametrize(
        "tab_locator, header_xpath, expected, is_default_tab",
        [
            (CONSTRUCTOR_TAB_FILLINGS, CONSTRUCTOR_TAB_FILLINGS[1], "Начинки", False),
            (CONSTRUCTOR_TAB_SAUCES, CONSTRUCTOR_TAB_SAUCES[1], "Соусы", False),
            (CONSTRUCTOR_TAB_BUNS, CONSTRUCTOR_TAB_BUNS[1], "Булки", True),
        ]
    )
    def test_tab_switch(self, browser, tab_locator, header_xpath, expected, is_default_tab):
        browser.get(BASE_URL)

        if not is_default_tab:
            browser.find_element(*tab_locator).click()
        header = browser.find_element(By.XPATH, header_xpath)

        assert expected in header.text
