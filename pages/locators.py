from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():

    AUTH_FORM = (By.ID, 'login_form')
    REG_FORM = (By.ID, 'register_form')
    LOGIN_LINK = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'


class ProductCardLocators():

    TEST_PRODUCT_URL = 'http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main>h1')
    PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main>p')
    BUTTON_ADD_BASKET = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, '.alertinner>strong')
    ADDED_PRICE = (By.CSS_SELECTOR, '.alertinner>p>strong')
    MESSAGE_ADD_TO_CARD = (By.CSS_SELECTOR, '.alertinner >strong')