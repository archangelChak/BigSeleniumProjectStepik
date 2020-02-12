from .pages.product_page import ProductPage
import pytest
from .pages.login_page import LoginPage

@pytest.mark.parametrize('link_finisher', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, link_finisher):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_finisher}"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_right_book()


@pytest.mark.xfail
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_cart()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_cart()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
