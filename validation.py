from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

"""
Not sure how to implement proper integration with other modules, need help
"""

#gets title from driver, returns true if they match, returns false if they don't
def validate_page_title(expected_title):
    title = driver.title
    return title == expected_title


#attempts to find specificed element, returns false if element is not found or if error occurs
def is_element_present(locator_type, locator_value):
    try:
        driver.find_element(locator_type, locator_value)
        return True
    except NoSuchElementException as e:
        print("Element not found: ", e)
        return False
