from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class ProductPage(Page):

    def open_product_page(self, product):
        self.driver.get('https://gettop.us/product/' + product)

    def
