from pages.base_page import Page
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

SEARCH_ICON = (By.CSS_SELECTOR, '.header__search')
SEARCH_BAR = (By. ID, "#Search-In-Modal")

ClICK_PRODUCT = (By. XPATH, '//a[@href="/products/cureskin-under-eye-gel?_pos=1&_sid=16a0e624b&_ss=r"]')


class SearchResults(Page):

    def product_click(self):
        self.click(*ClICK_PRODUCT)

