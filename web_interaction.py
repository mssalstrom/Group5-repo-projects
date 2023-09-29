from selenium import webdriver


# Initializes the WebDriver based on the browser type provided.
def initialize_driver(browser_type):
    if browser_type.lower() == 'chrome':
        # Initialize Chrome WebDriver
        driver = webdriver.Chrome()
    elif browser_type.lower() == 'firefox':
        # Initialize Firefox WebDriver
        driver = webdriver.Firefox()
    elif browser_type.lower() == 'edge':
        # Initialize Microsoft Edge WebDriver
        driver = webdriver.Edge()
    else:
        # Handle unsupported browser types or provide default behavior
        raise ValueError(f"Unsupported browser type: {browser_type}")

    return driver


# Uses the WebDriver instance to navigate to the provided URL.
def navigate_to_url(driver, url):
    driver.get(url)
