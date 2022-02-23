import pytest
from pages.basket_page import BasketPage
import time


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.guest_go_to_basket()
    page.not_product_in_basket()
    page.text_basket_is_empty()
