from selenium.webdriver.common.by import By

REGISTER_NAME_INPUT = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
# Поле "Имя" на форме регистрации

REGISTER_EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
# Поле "Email" на форме регистрации

REGISTER_PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
# Поле "Пароль" на форме регистрации

REGISTER_SUBMIT_BUTTON = (By.XPATH, '//button[contains(text(), "Зарегистрироваться")]')
# Кнопка "Зарегистрироваться"

REGISTER_ERROR_MESSAGE = (By.XPATH, '//p[@class="input__error text_type_main-default"]')
# Сообщение об ошибке на форме регистрации
