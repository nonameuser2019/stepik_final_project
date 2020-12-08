from selenium.common.exceptions import NoAlertPresentException
from .pages.product_page import ProductPage
from .pages.locators import ProductCardLocators
from .pages.base_page import BasePage
import selenium
import time
import pytest


@pytest.mark.parametrize('promo_code', range(10))
def test_guest_can_add_product_to_basket(browser, promo_code):
    PRODUCT_URL = ('http://selenium1py.pythonanywhere.com/catalogue/'
                   'coders-at-work_207/?promo=offer{}'.format(promo_code))
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.add_product_to_basket(browser)
    page.check_prod_name_in_basket(browser)


def test_check_correct_price_in_basket(browser):
    card_url = ProductCardLocators.TEST_PRODUCT_URL
    page = ProductPage(browser, card_url)
    page.open()
    page.add_product_to_basket(browser)
    page.check_coorect_price_in_basket(browser)

@pytest.mark.product_page
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductCardLocators.TEST_PRODUCT_URL)
    page.open()
    page.add_product_to_basket(browser)
    page.check_message_after_add_product_to_basket()

