from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch Firefox browser')
def launch_browser(context):
    """
    Initializes an instance of selenium webdriver
    Args:
        context: context variable

    Returns:
        none
    """
    context.driver = webdriver.Firefox()


@when('I open URL Shortener homepage')
def open_homepage(context):
    """
    Navigates to URL of web application
    Args:
        context: context variable
            Has an initialized instance of selenium driver as an attribute

    Returns:
        none
    """
    context.driver.get("http://localhost:5000/")


@when('verify that the title is "127.0.0.1:5000"')
def verify_title(context):
    """
    Ensure that the title matches the intended title
    Args:
        context:  context variable
            Has an initialized instance of selenium driver as an attribute

    Returns:
        none

    """
    assert context.driver.title == "127.0.0.1:5000"


@when('I enter the {url} url')
def enter_url(context, url):
    """
    Enters a URL into the appropriate text field
    Args:
        context: context variable
            Has an initialized instance of selenium driver as an attribute
        url: URL to be entered

    Returns:
        none
    """
    context.driver.find_element(By.NAME, "url").send_keys(url)


@when('enter shorten name "{sn}"')
def enter_short_name(context, sn):
    """
    Enter a shortened name into the appropriate text field
    Args:
        context: context variable
            Has an initialized instance of selenium driver as an attribute
        sn: Shortened name to be entered

    Returns:
        none
    """
    context.driver.find_element(By.NAME, "code").send_keys(sn)


@when('click on Shorten URL button')
def press_button_shorten_url(context):
    """
    Clicks on the form submit button
    Args:
        context: context variable
            Has an initialized instance of selenium driver as an attribute

    Returns:
        none
    """
    shorten_button = context.driver.find_element(By.ID, "shortenSubmit")
    # Click the button
    shorten_button.click()


@when('user can see new page with short link')
def verify_new_page(context):
    """
    Ensures that the program has navigated to the correct page
    Args:
        context: context variable
            Has an initialized instance of selenium driver as an attribute

    Returns:
        none
    """
    # check for elements, text, or any other criteria on this page.
    assert context.driver.title == "Your URL"


@when('I click on the link with id "return"')
def press_return_link(context):
    """
    Returns to the previous page
    Args:
        context: context variable
            Has an initialized instance of selenium driver as an attribute

    Returns:
        none
    """
    back_link = context.driver.find_element(By.ID, "return")
    back_link.click()


@then('successfully return to the home page')
def verify_home_page(context):
    """
    Ensures that the program has returned to the home page
    Args:
        context: context variable
            Has an initialized instance of selenium driver as an attribute

    Returns:
        none
    """
    assert context.driver.title == "URL Shortener", f"Expected title to be: {context.driver.title}"
    context.driver.close()
