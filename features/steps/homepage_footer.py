import time

from selenium.webdriver.common.by import By
from behave import given, when, then


@given('User is on homepage')
def open_homepage(context):
    context.app.homepage.open_homepage()


@given('Clicks on search icon')
def click_search_icon(context):
    context.app.homepage.click_search_icon()


@given('Clicks on search icon again')
def click_search_icon(context):
    context.app.homepage.click_search_icon_header()


@given('User searches for {goods}')
def search_input(context, goods):
    context.app.homepage.search_input(goods)



@when('User scrolls down to footer')
def scroll_to_footer(context):
    context.app.homepage.scroll_to_footer()


@when('Clicks {footer_link}')
def click_terms_of_service(context, footer_link):
    context.app.homepage.click_terms_of_service()


@then('Verify {expected_title} page opened')
def verify_links_page(context, expected_title):
    context.app.homepage.verify_links_page(expected_title)



