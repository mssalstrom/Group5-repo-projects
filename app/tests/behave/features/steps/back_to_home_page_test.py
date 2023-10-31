from behave import *
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

"""RTM REFERENCE: URL Shortener TC7, TC8"""

@given('I launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()

@when('open URL Shortener Home page')
def open_home_page(context):
    context.driver.get("http://localhost:5000/")
    context.driver.implicitly_wait(10)

@when ('I enter the "{url}" url')
def enter_url(context, url):
    context.driver.find_element(By.NAME, 'url').send_keys(url)

@when ('I enter shorten name "{short_name}"')
def enter_short_name(context, short_name):
    context.driver.find_element(By.NAME, 'code').send_keys(short_name)

@when ('click on the shorten url button')
def press_button(context):
    context.driver.find_element(By.ID, 'shortenSubmit').click()

@when ('I should be redirected to the /your_url page')
def step_impl(context):
    assert context.driver.title == "Your URL"

@when ('click on the back to home page button')
def press_button(context):
    context.driver.find_element(By.ID, 'backToHome').click()

@then ('user must be successfully redirected to the home page')
def step_impl(context):
    assert context.driver.title == "URL Shortener"
    context.driver.close()