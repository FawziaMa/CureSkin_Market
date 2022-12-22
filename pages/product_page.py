from pages.base_page import Page
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ProductPage(Page):

    def open_product_page(self, product):
        self.driver.get('https://shop.cureskin.com/products/cureskin-under-eye-gel?_pos=1&_sid=fc88dee3b&_ss=r')


