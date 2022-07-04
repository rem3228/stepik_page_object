from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/?promo=newYear'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_add_product_to_basket_button()
    product_page.should_be_product_name()
    product_page.should_be_product_price()
    product_page.click_on_add_product_to_basket_button()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_price_equal_to_product_price_in_basket()
    product_page.should_be_product_name_in_basket_success_alerts()

