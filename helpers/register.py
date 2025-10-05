from locators import *
from constants.site import BASE_URL


def go_to_registration_page(driver):
    driver.get(BASE_URL)
    driver.find_element(*MAIN_LOGIN_BUTTON).click()
    driver.find_element(*REGISTER_PAGE_LINK).click()
