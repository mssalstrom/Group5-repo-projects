from behave import *
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

"""RTM REFERENCE: URL Shortener TC1, TC2"""


@given('I launch browser')
def launch_browser(context):
    context.driver = webdriver.Firefox()


@when('I open URL Shortener Page')
def open_home_page(context):
    context.driver.get("http://localhost:5000/")


@when('I Enter url "{url}"')
def enter_url(context, url):
    context.driver.find_element(By.NAME, "url").send_keys(url)


@when('I Enter shorten name "{sn}"')
def enter_short_name(context, sn):

    context.driver.find_element(By.NAME, "code").send_keys(sn)


@when('I Select the Shorten URL button')
def press_button(context):
    context.driver.find_element(By.ID, "shortenSubmit").click()


@then('Go to the /your_url page')
def step_impl(context):
    assert context.driver.title == "Your URL"
    context.driver.close()







