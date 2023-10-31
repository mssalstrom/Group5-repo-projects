from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch Firefox browser')
def launch_browser(context):
    context.driver = webdriver.Firefox()


@when('I open URL Shortener homepage')
def open_homepage(context):
    context.driver.get("http://localhost:5000/")


@when('verify that the title is "127.0.0.1:5000"')
def verify_title(context):
    assert context.driver.title == "127.0.0.1:5000"


@when('I enter the {url} url')
def enter_url(context, url):
    context.driver.find_element(By.NAME, "url").send_keys(url)


@when('enter shorten name "{sn}"')
def enter_short_name(context, sn):
    context.driver.find_element(By.NAME, "code").send_keys(sn)


@when('click on Shorten URL button')
def press_button_shorten_url(context):
    shorten_button = context.driver.find_element(By.ID, "shortenSubmit")
    # Click the button
    shorten_button.click()


@when('user can see new page with short link')
def verify_new_page(context):
    # check for elements, text, or any other criteria on this page.
    assert context.driver.title == "Your URL"


@when('I click on the link with id "return"')
def press_return_button(context):
    back_link = context.driver.find_element(By.ID, "return")
    back_link.click()


@then('successfully return to the home page')
def verify_home_page(context):
    assert context.driver.title == "URL Shortener", f"Expected title to be: {context.driver.title}"
    context.driver.close()
