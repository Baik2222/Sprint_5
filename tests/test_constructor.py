from locators import *

from constants.site import BASE_URL


def test_constructor_tab_click_by_fillings(browser):
    browser.get(BASE_URL)

    browser.find_element(*CONSTRUCTOR_TAB_FILLINGS).click()
    fillings_header = browser.find_element(By.XPATH, '//h2[contains(text(), "Начинки")]')

    assert "Начинки" in fillings_header.text


def test_constructor_tab_click_by_sauces(browser):
    browser.get(BASE_URL)

    browser.find_element(*CONSTRUCTOR_TAB_SAUCES).click()
    sauces_header = browser.find_element(By.XPATH, '//h2[contains(text(), "Соусы")]')

    assert "Соусы" in sauces_header.text


def test_constructor_tab_click_by_buns(browser):
    browser.get(BASE_URL)

    buns_header = browser.find_element(By.XPATH, '//h2[contains(text(), "Булки")]')

    assert "Булки" in buns_header.text
