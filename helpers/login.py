from locators import *
from constants.site import BASE_URL


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
