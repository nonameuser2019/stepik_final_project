from .base_page import BasePage
from .locators import ProductCardLocators
from selenium import webdriver
from .locators import ProductCardLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.add_product_to_basket()

    def should_be_product_name(self, browser: webdriver.Chrome):
        assert self.is_element_present(*ProductCardLocators.PRODUCT_NAME), "Product name was not found"

    def should_be_price(self, browser):
        assert self.is_element_present(*ProductCardLocators.PRICE), "Price was not found"

    def should_be_add_to_basket_button(self, browser):
        assert self.is_element_present(*ProductCardLocators.BUTTON_ADD_BASKET), "Button add to basket was not found"

    def add_product_to_basket(self, browser: webdriver.Chrome):
        button_add_to_busket = browser.find_element(*ProductCardLocators.BUTTON_ADD_BASKET)
        button_add_to_busket.click()
        self.solve_quiz_and_get_code()

    def check_prod_name_in_basket(self, browser: webdriver.Chrome):
        product_name = browser.find_element(*ProductCardLocators.PRODUCT_NAME).text
        product_name_in_basket = browser.find_element(*ProductCardLocators.ADDED_PRODUCT_NAME).text
        assert product_name == product_name_in_basket, "The name of product in the basket isn't correct"

    def check_correct_price_in_basket(self, browser: webdriver.Chrome):
        price = browser.find_element(*ProductCardLocators.PRICE).text
        product_price_in_basket = browser.find_element(*ProductCardLocators.ADDED_PRICE).text
        assert price == product_price_in_basket, f"Price in basket isn't correct {price} != {product_price_in_basket}"

    def check_message_after_add_product_to_basket(self):
        assert self.is_not_element_present(*ProductCardLocators.MESSAGE_ADD_TO_CARD), \
            'The message that product is add to basket does not find'

    def check_message_disappeared_after_add_to_basket(self):
        assert self.is_disappeared(*ProductCardLocators.MESSAGE_ADD_TO_CARD), 'The message that product add' \
                                                                              'to cart not disappear'
