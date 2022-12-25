from pages.base_page import Page
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


FOOTER_LINKS = (By. XPATH, "//div[@class='footer-block grid__item footer-block--menu'][1]/ul/li/a")
SEARCH_ICON = (By.CSS_SELECTOR, '.header__search')
TERMS_PAGE_TITLE = (By.XPATH, "//*[text()='Terms of service']")
SEARCH_ICON_HEADER = (By. CSS_SELECTOR, '.search__button')

class Homepage(Page):
    SEARCH_BAR = (By.ID, "Search-In-Modal")
    # PAGE_TITLE = (By.XPATH, "//div[@class='shopify-policy__title']/h1['EXPECTED_TITLE']")

    def open_homepage(self):
        self.driver.get("https://shop.cureskin.com/")

    def scroll_to_footer(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_terms_of_service(self):
        self.driver.find_element(*FOOTER_LINKS).click()

    # def get_page_title_locator(self, expected_title: str):
    #     return[self.PAGE_TITLE[0], self.PAGE_TITLE[1].replace('EXPECTED_TITLE', expected_title)]
    def verify_links_page(self, expected_title):
        # title_page = self.get_page_title_locator(expected_title)
        # actual_title = title_page
        actual_title = self.driver.find_element(*TERMS_PAGE_TITLE).text
        assert actual_title == expected_title, f" Error expected {expected_title} but got {actual_title}"

    def click_search_icon(self):
        self.click(*SEARCH_ICON)

    def search_input(self, goods):
        self.input_text(goods, *self.SEARCH_BAR)

    def click_search_icon_header(self):
        self.click(*SEARCH_ICON_HEADER)

