from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_products_in_page(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT), \
            "Product is presented, but should not be"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT),\
            "Empty basket text is not presented"

