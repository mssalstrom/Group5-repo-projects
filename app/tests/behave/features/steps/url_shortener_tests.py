from behave import *
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

"""RTM REFERENCE: URL Shortener TC1, TC2"""


@given('I launch browser')
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


@when('I open URL Shortener Page')
def open_home_page(context):
    """
    Navigate to URL of application
    Args:
        context: context variable
            Has an initialized instance of selenium driver as an attribute

    Returns:
        none
    """
    context.driver.get("http://localhost:5000/")


@when('I Enter url "{url}"')
def enter_url(context, url):
    """
    Enter URL into appropriate text field
    Args:
        context: context variable
            Has an initialized instance of selenium driver as an attribute
        url: URL to be entered

    Returns:
        none
    """
    context.driver.find_element(By.NAME, "url").send_keys(url)


@when('I Enter shorten name "{sn}"')
def enter_short_name(context, sn):
    """
    Enter shortened name into appropriate text field
    Args:
        context: context variable
            Has an initialized instance of selenium driver as an attribute
        sn: Shortened name to be entered

    Returns:
        none
    """

    context.driver.find_element(By.NAME, "code").send_keys(sn)


@when('I Select the Shorten URL button')
def press_button(context):
    """
    Click form submit button
    Args:
        context: context variable
            Has an initialized instance of selenium driver as an attribute

    Returns:
        none
    """
    context.driver.find_element(By.ID, "shortenSubmit").click()


@then('Go to the /your_url page')
def step_impl(context):
    """
    Ensure that the shortened URL link navigates to the correct page
    Args:
        context: context variable
            Has an initialized instance of selenium driver as an attribute

    Returns:
        none
    """
    assert context.driver.title == "Your URL"
    context.driver.close()







