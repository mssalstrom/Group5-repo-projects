from behave import *
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@given('launch web browser')
def launch_browser(context):
    """
    Initialize an instance of selenium webdriver
    Args:
        context: context variable
            Has an initialized instance of selenium driver as an attribute

    Returns:
        none
    """
    context.driver = webdriver.Firefox()


@when('open URL Shortener Home page')
def open_home_page(context):
    """
    Navigates to URL of web application
    Args:
        context: context variable
            Has an initialized instance of selenium driver as an attribute

    Returns:
        none
    """
    context.driver.get("http://localhost:5000/")


@then('verify that the logo is present on page')
def check_logo(context):
    """
    Ensure that the logo is present on the webpage
    Args:
        context: context variable
            Has an initialized instance of selenium driver as an attribute

    Returns:
        none
    """
    context.driver.find_element(By.ID, 'wtccHeaderImage')


@then('close browser')
def close_browser(context):
    """
    Close the browser
    Args:
        context: context variable
            Has an initialized instance of selenium driver as an attribute

    Returns:
        none
    """
    context.driver.close()




