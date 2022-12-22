from selenium.webdriver.common.by import By
from behave import given, when, then


@then('User is taken to product page')
def open_product_page(context):
    context.app.product_page.open_product_page
