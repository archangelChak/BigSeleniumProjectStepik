from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_LIST), "There are products in the basket"

    def should_be_empty(self):
        assert "empty" in self.browser.find_element(*BasketPageLocators.BASKET_LIST_EMPTY).text, "Basket not emptu"