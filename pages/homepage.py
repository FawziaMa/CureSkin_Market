from pages.base_page import Page
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


TERMS_OF_SERVICE = (By. XPATH, "//a[@href='/policies/terms-of-service']")
TERMS_PAGE_TITLE = (By. XPATH, "//div[@class='shopify-policy__title']//h1['Terms of service']")


SEARCH_ICON = (By.CSS_SELECTOR, '.header__search')


class Homepage(Page):
    SEARCH_BAR = (By.ID, "Search-In-Modal")

    def open_homepage(self):
        self.driver.get("https://shop.cureskin.com/")

    def scroll_to_footer(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_terms_of_service(self):
        self.driver.find_element(*TERMS_OF_SERVICE).click()

    def verify_terms_page(self):
        self.driver.find_element(*TERMS_PAGE_TITLE).text()

    def click_search_icon(self):
        self.click(*SEARCH_ICON)

    def search_input(self, goods):
        self.input_text(goods, *self.SEARCH_BAR)
        self.click(*SEARCH_ICON)

