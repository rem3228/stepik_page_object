import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import faker

@pytest.mark.xfail
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
def test_user_cant_see_success_message_after_adding_product_to_basket( browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_on_add_product_to_basket_button()
    product_page.should_not_be_success_message()

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_add_product_to_basket_button()
    product_page.should_be_product_name()
    product_page.should_be_product_price()
    product_page.click_on_add_product_to_basket_button()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_price_equal_to_product_price_in_basket()
    product_page.should_be_product_name_in_basket_success_alerts()

@pytest.mark.xfail
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_on_add_product_to_basket_button()
    product_page.should_not_be_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_page()
    basket_page.should_be_empty_basket_text()

@pytest.mark.add_to_basket_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        f = faker.Faker()
        link = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.should_be_login_url()
        login_page.should_be_register_form()
        login_page.register_new_user(f.email(),f.password())
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_add_product_to_basket_button()
        product_page.should_be_product_name()
        product_page.should_be_product_price()
        product_page.click_on_add_product_to_basket_button()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_product_price_equal_to_product_price_in_basket()
        product_page.should_be_product_name_in_basket_success_alerts()