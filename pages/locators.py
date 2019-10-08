from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators(object):
    ADD_TO_BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_IN_BACKET_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRODUCT_IN_BACKET_PRICE = (By.CSS_SELECTOR, ".fade.in > div > p:nth-child(1) > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
