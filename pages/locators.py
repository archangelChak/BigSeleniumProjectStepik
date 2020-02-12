from selenium.webdriver.common.by import By


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, "button[value='Add to basket']")
    MESSG1 = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    MESSG3 = (By.CSS_SELECTOR,
              "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main >.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SHOPPING_CART = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs > span")

class BasketPageLocators():
    BASKET_LIST = (By.CSS_SELECTOR, ".basket-title.hidden-xs")
    BASKET_LIST_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")