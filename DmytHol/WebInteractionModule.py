from selenium import webdriver

class WebInteractionModule:
    def __init__(self, browser_type):
        self.driver = self.initialize_driver(browser_type)
        
    # Initializes the WebDriver based on the browser type provided.
    def initialize_driver(self, browser_type):
        if browser_type.lower() == 'chrome':
            # Initialize Chrome WebDriver
            driver = webdriver.Chrome()
        elif browser_type.lower() == 'firefox':
            # Initialize Firefox WebDriver
            driver = webdriver.Firefox()
        elif browser_type.lower() == 'safari':
            # Initialize Microsoft Edge WebDriver
            driver = webdriver.Safari()
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")

        return driver
    
    # Function to navigate to the provided URL.
    def navigate_to_url(self, url):
        self.driver.get(url)  # Using the driver instance initialized in __init__