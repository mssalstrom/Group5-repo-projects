from behave import *
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@given('launch web browser')
def launch_browser(context):
    context.driver = webdriver.Firefox()


@when('open URL Shortener Home page')
def open_home_page(context):
    context.driver.get("http://localhost:5000/")


@then('verify that the logo is present on page')
def check_logo(context):
    context.driver.find_element(By.ID, 'wtccHeaderImage')


@then('close browser')
def close_browser(context):
    context.driver.close()




