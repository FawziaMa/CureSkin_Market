from pages.base_page import Page
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ProductPage(Page):

    def open_product_page(self, product):
        self.driver.get('https://gettop.us/product/' + product)


