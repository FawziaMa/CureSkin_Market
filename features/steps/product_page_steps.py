import time

from selenium.webdriver.common.by import By
from behave import given, when, then


@then('User is taken to {expected_product} page')
def product_page(context, expected_product):
    context.app.product_page.verify_product_page(expected_product)

