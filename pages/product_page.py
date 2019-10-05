from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
import time


class ProductPage(BasePage):

    def should_be_add_to_backet_form(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_FORM), "Add to backet form is not presented"

    def click_add_to_backet_form(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_FORM), "Add to backet form is not presented"
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_FORM)
        button.click()
        self.solve_quiz_and_get_code()
        # time.sleep(3)

    def check_name_product(self):
        product_in_backet_name = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BACKET_NAME)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        # print(f'\n{product_in_backet_name.text}\n{product_name.text}')
        assert product_in_backet_name.text == product_name.text, "Product names do not match:("
        time.sleep(1)

    def check_price_product(self):
        product_in_backet_price = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BACKET_PRICE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        # print(f'\n{product_in_backet_name.text}\n{product_name.text}')
        assert product_in_backet_price.text == product_price.text, "Product price do not match:("
        time.sleep(1)
