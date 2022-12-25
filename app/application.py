from pages.homepage import Homepage
from pages.product_page import ProductPage
from pages.search_results import SearchResults


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.product_page = ProductPage(self.driver)
        self.homepage = Homepage(self.driver)
        self.search_results = SearchResults(self.driver)
