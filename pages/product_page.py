from pages.base_page import Page
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

EXPECTED_PRODUCT_URL = (By. XPATH, "//h1[@class='product__title'][contains(text(), 'CureSkin Under Eye Gel')]")


class ProductPage(Page):
    def verify_product_page(self, expected_product):
        actual_product = self.driver.find_element(*EXPECTED_PRODUCT_URL).text
        assert actual_product == expected_product


