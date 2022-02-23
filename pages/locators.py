from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
    PRODUCT_NAME_AFTER = (By.XPATH, "(//div[@class='alertinner ']/strong)[1]")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    BUSKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    ALLERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")