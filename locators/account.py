from selenium.webdriver.common.by import By

HEADER_PROFILE_BUTTON = (By.XPATH, '//a[contains(@href, "/account")]/p[text()="Личный Кабинет"]/..')
# Кнопка "Личный кабинет" в шапке

PROFILE_SECTION = (By.CLASS_NAME, 'AppHeader_header__link__3D_hX')
# Блок профиля после авторизации

PROFILE_LINK = (By.XPATH, '//a[contains(@href, "/account/profile") and contains(text(), "Профиль")]')
# Ссылка "Профиль" в меню профиля

PROFILE_LOGOUT_BUTTON = (By.XPATH, '//button[contains(@class, "Account_button__14Yp3") and text()="Выход"]')
# Кнопка "Выход" в профиле

PROFILE_NAME_FIELD = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
# Поле "Имя" в профиле
