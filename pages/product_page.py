from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            error_line = "Неверный ответ или закончилось время! Попробуйте запустить тест снова."
            assert not(error_line in alert_text), error_line
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_right_book(self):
        message1 = self.browser.find_element(*ProductPageLocators.MESSG1).text
        message2 = self.browser.find_element(*ProductPageLocators.MESSG3).text
        assert (message1, message2) == (self.get_book_name(), self.get_book_price()), "We've got he wrong book Carl"

    def get_book_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text

    def get_book_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text

    def click_add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart_button.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
