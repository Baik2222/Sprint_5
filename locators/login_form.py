from selenium.webdriver.common.by import By

LOGIN_EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
# Поле "Email" на форме входа

LOGIN_PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
# Поле "Пароль" на форме входа

LOGIN_SUBMIT_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')
# Кнопка "Войти" на форме входа

LOGIN_ERROR_MESSAGE = (By.XPATH, '//p[@class="input__error text_type_main-default"]')
# Сообщение об ошибке на форме входа
