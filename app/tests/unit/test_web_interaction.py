# test_web_interaction
import os
import pathlib
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Fixture setup, initialize driver instance and navigate to URL
@pytest.fixture
def setup_data():
    """
    Fixture setup, initialize driver instance and navigate to URL

    Returns:
        instance of selenium webdriver
    """
    print("\nSetting up Resources")
    driver = webdriver.Firefox()
    driver.get("http://localhost:5000/")
    return driver


@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    """
      Fixture for session-level cleanup after all tests.

      This fixture automatically performs teardown operations at the end of the test session.
      It removes the specified files '../urls.json', 'test_screenshot.png' if they exist.

      Usage:
          This fixture is designed with the 'session' scope, meaning it runs once per test session.
          It is applied automatically to all tests due to the 'autouse=True' parameter.
      """
    def tear_down():
        print("\nPerforming Teardown")
        path = pathlib.Path('../urls.json')
        if path:
            os.remove(path)
        if os.path.exists('test_screenshot.png'):
            os.remove('test_screenshot.png')
    request.addfinalizer(tear_down)


def test_validate_page_title(setup_data):
    """
    Test if the URL of the page matches the expected URL

    Params:
        driver: an instance of selenium webdriver

    Returns:
        none
    """
    expected_title = "URL Shortener"
    try:
        assert setup_data.title == expected_title, "Page title does not match expected title."
    finally:
        time.sleep(1)
        setup_data.close()


def test_url_shortener(setup_data):
    """
    Tests if the URL shortener is functioning properly

    Params:
        driver: an instance of selenium webdriver

    Returns:
        none
    """
    # Enter URL into URL element
    url = setup_data.find_element(By.NAME, "url")
    url.clear()
    url.send_keys("https://blackboard.waketech.edu/webapps/login/")
    # Enter shortened name
    shortened_name = "Blackboard"
    code = setup_data.find_element(By.NAME, "code")
    code.clear()
    code.send_keys(shortened_name)
    submit = setup_data.find_element(By.ID, "shortenSubmit")
    submit.click()
    time.sleep(5)
    # Ensure that the name displayed on the new page is the same as the shortened name
    code_name = setup_data.find_element(By.TAG_NAME, "h2")
    assert code_name.text == shortened_name, "Code name does not match shortened name entered."
    setup_data.back()
    setup_data.refresh()
    # Ensure that the link at the bottom of the page returns the user to the correct site
    new_code = setup_data.find_element(By.LINK_TEXT, shortened_name)
    new_code.click()
    try:
        assert setup_data.title == "Blackboard Learn", "Page title does not match expected title."
    finally:
        time.sleep(1)
        setup_data.close()


def test_filename_shortener(setup_data):
    """
    Tests if the filename shortener is functioning properly

    Params:
        driver: an instance of selenium webdriver

    Returns:
        none
    """
    # Grabs txt file from current folder
    file_path = os.path.join(os.getcwd(), "File.txt")

    # use selenium to input file in filename shortener
    fileInput = setup_data.find_element(By.ID, "fileInput")
    fileInput.clear()
    fileInput.send_keys(file_path)

    # sets file name to Test File
    expected_name = "Test File"
    file_name = setup_data.find_element(By.ID, "codeName")
    file_name.clear()
    file_name.send_keys("Test File")

    # clicks button and adds file to json
    saveImageElement = setup_data.find_element(By.ID, "saveImage")
    saveImageElement.click()

    # asserts name is correctly entered
    code_name = setup_data.find_element(By.TAG_NAME, "h2")
    try:
        assert code_name.text == expected_name, "Code name does not match shortened name entered."
    finally:
        time.sleep(1)
        setup_data.close()



