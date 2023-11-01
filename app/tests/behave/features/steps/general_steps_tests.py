from behave import *
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@given('I launch web browser')
def launch_browser(context):
    context.driver = webdriver.Firefox()


@when('I open URL shortener')
def open_home_page(context):
    context.driver.get("http://localhost:5000/")


@then('I verify url was shortened')
def step_impl(context):
    assert context.driver.title == "Your URL"


@then('I close browser')
def close_browser(context):
    context.driver.close()
