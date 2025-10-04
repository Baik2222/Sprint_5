from selenium.webdriver.common.by import By

MAIN_LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти в аккаунт")]')
# Кнопка "Войти в аккаунт" на главной

REGISTER_PAGE_LINK = (By.XPATH, '//a[contains(@href,"/register")]')
# Ссылка на регистрацию

LOGIN_LINK_ON_REGISTER_PAGE = (By.XPATH, '//a[contains(@href, "/login") and text()="Войти"]')
# Кнопка "Войти" на странице регистрации
