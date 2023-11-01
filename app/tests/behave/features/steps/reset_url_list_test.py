from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


# Initialize the WebDriver
@given('I am on the URL Shortener page')
def open_url_shortener(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5000/")


@when('I check if the "Reset URL List" button exists')
def check_reset_button_exists(context):
    # Check if the button with the provided text exists
    reset_buttons = context.driver.find_elements(By.CLASS_NAME, "reset-button")
    context.reset_button_exists = len(reset_buttons) > 0


@when('I click the "Reset URL List" button')
def click_reset_button(context):
    if context.reset_button_exists:
        reset_button = context.driver.find_element(By.CLASS_NAME, "reset-button")
        reset_button.click()


@when('the URL list should be cleared')
def verify_url_list_cleared(context):
    # Check if the "Reset URL List" button is not present
    reset_buttons = context.driver.find_elements(By.CLASS_NAME, "reset-button")
    assert len(reset_buttons) == 0


@then('I should be redirected to the home page')
def verify_redirected_to_home_page(context):
    # Implement logic to verify if the user is redirected to the home page
    # For example, you can check the page title or other relevant elements on the home page
    assert context.driver.title == "URL Shortener"
