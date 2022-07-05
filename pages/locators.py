from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[contains(@class, 'basket')]")
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    PRODUCT_PRICE = (By.XPATH, "//p[contains(@class, 'price_color')]")
    BASKET_SUCCESS_ALERTS = (By.XPATH, "//div[contains(@class, 'alert-success')]/div[contains(@class, 'alertinner')]/strong")
    BASKET = (By.XPATH, "//div[contains(@class, 'basket')]")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//span/a[contains(@href, 'basket')]")

class BasketPageLocators():
    PRODUCT = (By.XPATH, "//div[contains(@class, 'basket-items')]")
    EMPTY_BASKET_TEXT = (By.XPATH, "//div[contains(@id,'content_inner')]/p")