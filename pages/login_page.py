from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This is not login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self, email=(str(time.time()) + "@fake.ru"), password=str(time.time())):
        email = (str(time.time()) + "@fake.ru")
        password = str(time.time())
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT)
        password_input1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1_INPUT)
        password_input2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2_INPUT)
        email_input.send_keys(email)
        password_input1.send_keys(password)
        password_input2.send_keys(password)
        submit = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        submit.click()
