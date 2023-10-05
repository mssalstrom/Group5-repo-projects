from selenium.common.exceptions import NoSuchElementException

class ValidationModule:
    def __init__(self, driver):
        self.driver = driver
        
    # Function to Validate Page Title
    def validate_page_title(self, expected_title):
        try:
            actual_title = self.driver.title
            return actual_title == expected_title
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False
        
    # Function to Validate Element Presence
    def is_element_present(self, locator_type, locator_value):
        try:
            element = self.driver.find_element(locator_type, locator_value)
            return True
        except NoSuchElementException:
            return False
