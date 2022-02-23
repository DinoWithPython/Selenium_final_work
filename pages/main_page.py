from .base_page import BasePage
from .locators import MainPageLocators
# from .login_page import LoginPage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


    def guest_go_to_basket(self):
        click_buton_basket = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
        click_buton_basket.click()


    def not_product_in_basket(self):
        assert self.is_not_element_present(*MainPageLocators.BASKET_SUMMARY), "Basket is not empty after click button!"
        
    
    def text_basket_is_empty(self):
        assert self.is_element_present(*MainPageLocators.BASKET_IS_EMPTY), "No text that the basket is empty"
        