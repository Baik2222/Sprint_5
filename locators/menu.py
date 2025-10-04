from selenium.webdriver.common.by import By

CONSTRUCTOR_TAB_BUNS = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG")][span[text()="Булки"]]')
# Вкладка "Булки"

CONSTRUCTOR_TAB_SAUCES = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG")][span[text()="Соусы"]]')
# Вкладка "Соусы"

CONSTRUCTOR_TAB_FILLINGS = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG")][span[text()="Начинки"]]')
# Вкладка "Начинки"

CONSTRUCTOR_HEADER = (By.XPATH, '//h1[contains(text(), "Соберите бургер")]')
# Заголовок конструктора

LOGO = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')
# Логотип Stellar Burgers для перехода на главную

CONSTRUCTOR_MENU = (By.XPATH, '//p[contains(text(),"Конструктор")]/ancestor::a')
# Кнопка "Конструктор" в шапке
