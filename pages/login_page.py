from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Login link is not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        # print(*LoginPageLocators.REGISTER_EMAIL)
        input1 = self.browser.find_element_by_css_selector(LoginPageLocators.REGISTER_EMAIL[1])
        input1.send_keys(email)
        input2 = self.browser.find_element_by_css_selector(LoginPageLocators.REGISTER_PASSWORD1[1])
        input2.send_keys(password)
        input3 = self.browser.find_element_by_css_selector(LoginPageLocators.REGISTER_PASSWORD2[1])
        input3.send_keys(password)

        button = self.browser.find_element_by_css_selector(LoginPageLocators.REGISTER_BUTTON[1])
        button.click()
