# test_examples.py
# Importing the necessary Playwright functions for synchronous operation
from playwright.sync_api import sync_playwright, expect


# Function to capture a screenshot of a web page
def test_screenshot():
    # Using 'sync_playwright' to create a synchronous Playwright context
    with sync_playwright() as p:
        # Launching a Chromium browser (Replace 'chromium' with your preferred browser)
        # Options: 'firefox', 'webkit' (for Firefox and WebKit respectively)
        browser = p.chromium.launch()
        # Creating a new page in the browser
        page = browser.new_page()
        # Navigating to the specified URL
        page.goto('https://www.saucedemo.com/')
        # Taking a screenshot and saving it to the specified path
        page.screenshot(path='test_screenshot.png')
        # Closing the browser
        browser.close()


def test_web_interaction():
    # Using 'sync_playwright' to create a synchronous Playwright context
    with sync_playwright() as p:
        # Launching a Chromium browser (Replace 'chromium' with your preferred browser)
        # Options: 'firefox', 'webkit' (for Firefox and WebKit respectively)
        browser = p.chromium.launch()
        # Creating a new page in the browser
        page = browser.new_page()
        # Navigating to the specified URL
        page.goto('https://www.saucedemo.com/')
        # Filling in the username field with 'standard_user'
        page.fill('input[id="user-name"]', 'standard_user')
        # Filling in the password field with 'secret_sauce'
        page.fill('input[id="password"]', 'secret_sauce')
        # Clicking the login button
        page.click('input[name="login-button"]')
        # Expecting the text 'Swag Labs' to be visible on the page
        expect(page.locator('Swag Labs')).to_be_visible()
        # Closing the browser
        browser.close()


def test_response():
    # Using 'sync_playwright' to create a synchronous Playwright context
    with sync_playwright() as p:
        # Launching a Chromium browser (Replace 'chromium' with your preferred browser)
        # Options: 'firefox', 'webkit' (for Firefox and WebKit respectively)
        browser = p.chromium.launch()
        # Creating a new page in the browser
        page = browser.new_page()
        # Making a GET request to the specified URL and capturing the response
        response = page.request.get('https://www.saucedemo.com/')
        # Expecting the response to be successful (HTTP status code 200)
        expect(response).to_be_ok()


def test_submit_fail():
    # Using 'sync_playwright' to create a synchronous Playwright context
    with sync_playwright() as p:
        # Launching a Chromium browser (Replace 'chromium' with your preferred browser)
        # Options: 'firefox', 'webkit' (for Firefox and WebKit respectively)
        browser = p.chromium.launch()
        # Creating a new page in the browser
        page = browser.new_page()
        # Navigating to the specified URL
        page.goto('https://www.saucedemo.com/')
        # Clicking the login button without entering credentials
        page.click('input[name="login-button"]')
        # Expecting the page to contain a specified text related to failed submission
        expect(page.locator("h3")).to_have_text("Epic sadface: Username is required")
        # Taking a screenshot of the page after the failed submission
        page.screenshot(path='submit_fail.png')


