from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
@given('I am on the URL Shortener page')
def open_url_shortener(context):
    context.driver = webdriver.Firefox()
    context.driver.get("http://localhost:5000/")

@when('I check if the "Reset URL List" button exists')
def check_reset_button_exists(context):
    # Check if the button with the provided text exists
    try:
        context.driver.find_element(By.ID, "resetButton")
        context.reset_button_exists = True
    except:
        context.reset_button_exists = False

@when('I click the "Reset URL List" button')
def click_reset_button(context, button_text):
    if context.reset_button_exists:
        reset_button = context.driver.find_element(By.ID, "resetButton")
        reset_button.click()

@then('the URL list should be cleared')
def verify_url_list_cleared(context):
    # Implement the logic to verify if the URL list is cleared
    # You can check if the list is empty or not present in the DOM
    pass
@then('I should be redirected to the home page')
def verify_redirected_to_home_page(context):
    # Implement the logic to verify if the user is redirected to the home page
    # You can check the page title or other relevant elements
    pass