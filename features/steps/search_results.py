import time

from pages.base_page import Page
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

ALL_PRODUCTS = (By. ID, '#ProductGridContainer')

# @when('User clicks on a product')
# def product_click(context):
#     all_product = context.driver.find_elements(*ALL_PRODUCTS)
#     for product in all_product:
#
#     context.app.SearchResults.product_click()
#
#
#
