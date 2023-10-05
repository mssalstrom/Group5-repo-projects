from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import FirefoxOptions

class WebDriverSetup:
    # Initializes the WebDriver based on the browser type provided.
    def initialize_driver(self, browser_type):
        if browser_type.lower() == 'chrome':
            # Initialize Chrome WebDriver
            chrome_options = Options()
        elif browser_type.lower() == 'firefox':
            # Initialize Firefox WebDriver
            firefox_options = FirefoxOptions()
        elif browser_type.lower() == 'edge':
            # Initialize Microsoft Edge WebDriver
            driver = webdriver.Edge()
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")

        return driver
    
    # Function to navigate to the provided URL.
    def navigate_to_url(self, driver, url):
        driver.get(url)