from .base_page import BasePage
from .locators import ProductPageLocators
# from .login_page import LoginPage

class ProductPage(BasePage): 
    def should_be_add_basket_form(self):
        assert self.is_element_present(*ProductPageLocators.ADD_FORM), "Add form is not presented"
    
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
        
    def product_name_after_add(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_after = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_AFTER).text
        assert product_name == product_name_after, "Product name is different!"
        
    def price_bassket_is_price_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        busket_price = self.browser.find_element(*ProductPageLocators.BUSKET_PRICE).text
        assert product_price == busket_price, "Prices are not equal!"
        
        
