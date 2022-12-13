from pages.product_page import ProductPage
from pages.homepage import Homepage
from pages.product_page import ProductPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.product_page = ProductPage(self.driver)
        self.homepage = Homepage(self.driver)
