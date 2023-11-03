# test_web_interaction

import os
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Fixture setup, initialize driver instance and navigate to URL
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get("http://localhost:5000/")
    return driver


def test_validate_page_title(driver):
    """Test if the URL of the page matches the expected URL"""
    expected_title = "URL Shortener"
    try:
        assert driver.title == expected_title, "Page title does not match expected title."
    finally:
        time.sleep(1)
        driver.close()


def test_url_shortener(driver):
    """Tests if the URL shortener is functioning properly"""
    # Enter URL into URL element
    url = driver.find_element(By.NAME, "url")
    url.clear()
    url.send_keys("https://blackboard.waketech.edu/webapps/login/")
    # Enter shortened name
    shortened_name = "Blackboard"
    code = driver.find_element(By.NAME, "code")
    code.clear()
    code.send_keys(shortened_name)
    URLsubmit = driver.find_element(By.ID, "URLSubmit")
    URLsubmit.click()
    time.sleep(5)
    # Ensure that the name displayed on the new page is the same as the shortened name
    code_name = driver.find_element(By.TAG_NAME, "h2")
    assert code_name.text == shortened_name, "Code name does not match shortened name entered."
    driver.back()
    driver.refresh()
    # Ensure that the link at the bottom of the page returns the user to the correct site
    new_code = driver.find_element(By.LINK_TEXT, shortened_name)
    new_code.click()
    try:
        assert driver.title == "Blackboard Learn", "Page title does not match expected title."
    finally:
        time.sleep(1)
        driver.close()


def test_filename_shortener(driver):
    """Tests if the filename shortener is functioning properly"""
    # Grabs txt file from current folder
    file_path = os.path.join(os.getcwd(), "File.txt")

    # use selenium to input file in filename shortener
    fileInput = driver.find_element(By.ID, "fileInput")
    fileInput.clear()
    fileInput.send_keys(file_path)

    # sets file name to Test File
    expected_name = "Test File"
    file_name = driver.find_element(By.ID, "codeName")
    file_name.clear()
    file_name.send_keys("Test File")

    # clicks button and adds file to json
    FileSubmitElement = driver.find_element(By.ID, "FileSubmit")
    FileSubmitElement.click()

    # asserts name is correctly entered
    code_name = driver.find_element(By.TAG_NAME, "h2")
    try:
        assert code_name.text == expected_name, "Code name does not match shortened name entered."
    finally:
        time.sleep(1)
        driver.close()


def test_clear_codes(driver):
    """Tests if the clear button functions properly"""
    pass
