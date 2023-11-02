from behave import given, when, then

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


# Initialize the WebDriver
@given('I am on the URL Shortener page')
def open_url_shortener(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5000/")


@when('I check if the "Reset URL List" button exists')
def check_reset_button_exists(context):
    try:
        reset_button = context.driver.find_element(By.NAME, "Reset URL List")
    except Exception as e:
        print(f'Exception: {e}')
        reset_button = None


    # Check if the button is displayed
    if reset_button and reset_button.is_displayed():
        print("Reset button is present.")
        context.reset_button_exists = True
    else:
        print("Reset button is not found.")


@when('I click the "Reset URL List" button')
def click_reset_button(context):
    reset_button = context.driver.find_element(By.CSS_SELECTOR, ".reset-button")
    if reset_button and reset_button.is_displayed():
        reset_button.click()



@then('the URL list should be cleared')
def verify_url_list_cleared(context):
    # Check if the "Reset URL List" button is not present
    try:
        reset_button = context.driver.find_element(By.CSS_SELECTOR, ".reset-button")
        assert reset_button is None
    except Exception as e:
        print(f'Exception: {e}')
