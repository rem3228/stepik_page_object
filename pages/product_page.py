from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_on_add_product_to_basket_button(self):
        add_product_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_product_to_basket_button.click()

    def should_be_add_product_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"

    def should_be_product_name(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def should_be_product_price(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_basket_success_alert(self):
        return self.browser.find_elements(*ProductPageLocators.BASKET_SUCCESS_ALERTS)[0].text

    def get_basket_product_price(self):
        return self.browser.find_element(*ProductPageLocators.BASKET).text.split()[2]

    def should_be_product_price_equal_to_product_price_in_basket(self):
        print(self.get_basket_product_price())
        assert self.get_product_price() == self.get_basket_product_price() \
            , "Product price not equal to product price in basket"

    def should_be_product_name_in_basket_success_alerts(self):
        print(self.get_basket_success_alert())
        assert self.get_product_name() == self.get_basket_success_alert() \
            , "Product not added to basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_SUCCESS_ALERTS), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_SUCCESS_ALERTS), \
            "Success message is presented, but should not be"