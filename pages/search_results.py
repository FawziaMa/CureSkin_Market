from pages.base_page import Page
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


PRODUCT = (By. XPATH, "//a[contains(text(), 'Under Eye Gel')]")


class SearchResults(Page):
    def product_click(self):
        self.click(*PRODUCT)

