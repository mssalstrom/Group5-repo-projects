

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
![Commits][commit-shield]
![pypi-shield]

<br />
<div align="center">
    <h1 align="center">CSC 256 Group 5 Project Readme</h1>
</div>



<!-- TABLE OF CONTENTS -->

# Table of Contents:
- [Introduction](#Introduction)
- [Selenium](#Selenium)
- [Setup](#setup)
- [Basics](#Basics)
- [UnitTest](#UnitTest)
- [BDD](#BDD)


<!-- ABOUT THE PROJECT -->
# Introduction
### Purpose 
> This document provides detailed instructions for testing a provided web application using selenium. Selenium is a library and suite of tools used to build test for web applications.

### Contributers 
- Dmytro Holovnia - Developer
- Matthew Salstrom - Developer
- Max Tart - Developer
- Dylan Arone - Tester
- Ian Kepplinger - Tester
- Ever Morales Alverez Tester
- Denitri Douglas - Document Writer
- Keven Hernandez Gaspar - Document Writer
- Eric Dixon - Document Writer
    
### Tools Used: 
- Python
- Selenium
- Flask

# Selenium
Selenium empowers developers and quality assurance teams to automate the testing of web applications by using Python scripts to interact with web elements, simulate user interactions, and validate the functionality and user experience of web pages, ensuring that the application works as intended and functions consistently across various browsers and browser versions. It serves as a versatile tool for functional testing, regression testing, and cross-browser testing, enabling efficient and repeatable testing processes integrated into software development workflows.

# Setup

### Download Selenium Branch
1. Open your preferred web browser and go to the Selenium GitHub repository: https://github.com/mssalstrom/Group5-repo-projects/tree/selenium.
2. On the repository page, click on the green "Code" button located near the top-right corner.
3. From the dropdown menu, click on "Download ZIP" to download the Selenium branch as a compressed ZIP file.
4. Once the ZIP file is downloaded, locate it on your computer and extract its contents to a desired location. This will create a folder containing the Selenium branch files.

### Installing Required Dependencies
1. Open your Python IDE (Integrated Development Environment) and navigate to the folder containing the extracted Selenium branch files.
2. Open the file app.py
3. In the terminal or command prompt, run the following command to install the required dependencies:
  
>In python terminal
```cmd
pip install -r requirements.txt
```

### Verify package installation: 
```cmd
flask --version
```
On Windows:
```cmd
python -m pip show selenium
```
On Mac:
```cmd
pip3 show selenium
```
- Expected outcome: *The command should display the version information of Flask, indicating that it has been installed correctly. There should be no errors or warnings.*
- If you do encounter errors proceed with the individual installations below, if not skip to the "Basics" section.
  
### Installing Flask: 
```cmd
pip install flask
```
```cmd
flask --version
```

### Installing Selenium: 
On Windows: 
```cmd
python -m pip install selenium
```
On Mac:
```cmd
pip3 install selenium
```
### Verify Selenium Installation: 
On Windows:
```cmd
python -m pip show selenium
```
On Mac:
```cmd
pip3 show selenium
```
- Expected outcome: *The command should display information about the Selenium package, including the version number, indicating that it has been installed correctly. There should be no errors or warnings.*

### Launch the Flask Web Application
1. In your Python IDE, open the app.py file.
2. Run the app.py file using the appropriate command or IDE feature to start the Flask server.
3. After running the app.py file, switch to the Python terminal or console within your IDE. This is where you will see the server startup message.
4. In the Python terminal, you should see the message "*Running on http://127.0.0.1:5000".
5. Open your web browser and enter the following URL in the address bar: http://127.0.0.1:5000.
6. Press Enter to access the web application.
7. If the web application "URL Shortener" opens successfully, you have set up the lab correctly. If not, review the above steps to ensure that Flask and Selenium are installed correctly.

Below are a series of test in the selenium suite of tools that can be used to automate test for a python web application. 

- Create a new python file named "seleniumLab.py" in the test directory. 

### Basics
**1. Using Selenium to test link navigation:**
- Import libraries
```python
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
```


- #### Create webdriver object
```python
#Create a WebDriver object for the Microsoft Edge browser
driver = webdriver.Edge()
```
- #### Set window size
```python
#Set the window size of the web browser to 800 pixels in width and 800 pixels in height
driver.set_window_size(800, 800)
```
```python
# Define the URL of the local web application you want to interact with
local_url = "localhost:5000"
```

- #### Launching link: 
```python
d# Navigate the web browser to the specified local URL
driver.get(local_url)  # Expected outcome: browser should navigate to the link

```


&#160;&#160;&#160;Expected outcome: *browser should navigate to link*

**2. Using Selenium to find elements:**  

```python
# Locate the HTML element with the "name" attribute set to "url" using Selenium's find_element method
url_element = driver.find_element(By.NAME, "url")
```
```python
# Locate the HTML element with the "name" attribute set to "code" using Selenium's find_element method
code_element = driver.find_element(By.NAME, "code")
```
```python
# Locate the HTML element with the "ID" attribute set to "shortenSubmit" using Selenium's find_element method
submit_button = driver.find_element(By.ID, "shortenSubmit")
```
**3. Using Selenium to test website functionality:**  

- Clear preexisitng text and type python.org into url shortener
```python
# Clear any preexisting text or input in the "url_element" field
url_element.clear()
```
```python
# Enter the URL "https://python.org" into the "url_element" input field
url_element.send_keys("https://python.org")
```

- Clear preexisitng text and type python as shortened url
```python  
# Clear any preexisting text or input in the "code_element" field
code_element.clear()
```

```python
# Enter the text "python" into the "code_element" input field
code_element.send_keys("python")
```
- Click submit

```python
# Simulate a click action on the "submit_button" element
submit_button.click()
```


- Wait 10s to verify page
```python
# Pause the script's execution for 10 seconds to allow time for the page to load or for verification
time.sleep(10)
```
- Go back to homepage

- Testing file input 
```python
# Navigate the web browser to the "local_url" to return to the homepage or a specific URL
driver.get(local_url)
```
```python
# Locate the HTML element with the "ID" attribute set to "fileInput" using Selenium's find_element method
fileElement = driver.find_element(By.ID, "fileInput")
```
```python
# Simulate selecting a file by sending the file path to the "fileElement" input field
fileElement.send_keys(file_path)
```
```python
# Locate the HTML element with the "ID" attribute set to "codeName" using Selenium's find_element method
codeNameElement = driver.find_element(By.ID, "codeName")
```
```python
# Enter the text "Shortname" into the "codeNameElement" input field
codeNameElement.send_keys("Shortname")
```
```python
time.sleep(10)
```


- Retesting with longer URL
- Clear preexisitng text and type python.org into url shortener
```python
url_element.clear()
```
```python
url_element.send_keys("[https://python.org](https://www.cnn.com/2023/02/09/us/iyw-puppy-bowl-shelters-rescue-groups/index.html)")
```

- Clear preexisitng text and type python as shortened url
```python  
code_element.clear()
```

```python
code_element.send_keys("puppyBowl")
```
- Click submit

```python
submit_button.click()
```


- Wait 10s to verify page
```python
time.sleep(10)
```
- Go back to homepage
  
```python
driver.get(local_url)
```
- Testing file input
```python
fileElement = driver.find_element(By.ID, "fileInput")
```
```python
fileElement.send_keys(file_path)
```
```python
codeNameElement = driver.find_element(By.ID, "codeName")
```
```python
codeNameElement.send_keys("Shortname")
```
```python
time.sleep(10)
```

### UnitTest
Selenin's strength is the ability to automate test. Below is an exmaple of a UnitTest using the selenium library
- Create a file named UnitTest.py in the test directory
 - Import necessary libraries
```cmd
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
```
- Create a class that inherits the TestCase class

```python
class urlShortener(unittest.TestCase):
```
- Initialize the webdriver
```python
    def setUp(self):
        self.driver = webdriver.Edge()
```
- Declare the test case method
```python
    def test_urlShortener(self):
```
- Set the driver
```python
        driver = self.driver
```
- Navigate to web application
```python
        driver.get("localhost:5000")
```
- Assertion to confirm site title
```python
        self.assertIn("urlShortener", driver.title)
```
- locate elements in page
```python
        url_element = driver.find_element(By.NAME, "url")
        code_element = driver.find_element(By.NAME, "code")
        submit_button = driver.find_element(By.ID, "shortenSubmit")

```
- Send data
```python
        url_element.clear()
        url_element.send_keys("https://python.org")
        submit_button.click()

        
```
- Wait to verify page
```python
        time.sleep(10)   
```
- Close driver
```python
    def tearDown(self):
        self.driver.close()
```
- Execute test
```python
if __name__ == "__main__":
    unittest.main()
```
# BDD

## Behavior-Driven Development (BDD)

**Behavior-Driven Development (BDD)** is a software development methodology that focuses on collaboration between technical and non-technical team members to improve the understanding of the desired behavior of a software system. BDD emphasizes using natural language descriptions to express the expected behavior of the system, making it accessible to non-technical stakeholders. It helps in aligning development efforts with business objectives and promotes a shared understanding of the software's features.

Key aspects of BDD include:

1. **Natural Language Specifications**: BDD encourages writing specifications in plain, human-readable language, often using a structured format like Gherkin. This language can be understood by both technical and non-technical team members.

2. **Collaboration**: BDD promotes collaboration between developers, testers, business analysts, and other stakeholders to define, validate, and document requirements.

3. **Examples and Scenarios**: BDD uses concrete examples and scenarios to illustrate the desired behavior of the system, making it easier to understand and test.

4. **Test-Driven Development (TDD)**: BDD often integrates with TDD, with the behavioral specifications serving as high-level tests that guide the development process.

5. **Automated Testing**: BDD encourages the automation of tests based on the specified behavior. These tests help ensure that the software functions as expected throughout the development process.

## Behave

**Behave** is a Python library that facilitates BDD by allowing you to write and execute behavioral tests using Gherkin language specifications. Behave acts as the bridge between plain language specifications (Gherkin) and Python code. It provides the framework to define Gherkin scenarios and the associated Python code that implements the steps of those scenarios.

Here are the steps to add Behave tests and Gherkin specifications to test a Flask application using Selenium:

1. **Install Behave**:
   If you haven't already, install Behave using pip:

   ```bash
   pip install behave
   ```

2. **Create Feature Files**:
   Feature files are written in Gherkin language and describe the behavior of your application. You can create feature files for different parts of your application. For example, create a `your_app.feature` file in the dedicated folder for your Behave tests.

   ```gherkin
   Feature: Testing Your Flask Application

   Scenario: Accessing the homepage
       Given the Flask application is running
       When I access the homepage
       Then I should see "Welcome to My Flask App" on the page

   Scenario: Shortening a URL
       Given I am on the homepage
       When I enter a long URL and a short code
       And I submit the form
       Then I should see a success message
   ```

3. **Implement Step Definitions**:
   Step definitions are Python functions that map the Gherkin steps to actions in your application. Create a Python file (e.g., `your_app_steps.py`) in the same folder as your feature files and define step definitions.

   ```python
   from behave import *

   @given("the Flask application is running")
   def step_flask_app_running(context):
       # Implement code to start your Flask application or set up the testing environment
       context.driver = webdriver.Edge()
       context.driver.set_window_size(800, 800)


   @when("I access the homepage")
   def step_access_homepage(context):
       # Implement code to navigate to the homepage using Selenium
       context.driver.get("http://localhost:5000")


   @then('I should see "{text}" on the page')
   def step_check_page_text(context, text):
       # Implement code to check if the specified text is present on the page
       page_source = context.driver.page_source
       assert text in page_source

   @when("I enter a long URL and a short code")
   def step_enter_long_url_and_short_code(context):
       # Implement code to interact with the URL shortening form
       url_element = context.driver.find_element(By.NAME, "url")
       url_element.clear()
       url_element.send_keys("https://python.org")

   @when("I submit the form")
   def step_submit_form(context):
       # Implement code to submit the form using Selenium
       submit_button = context.driver.find_element(By.ID, "shortenSubmit")
       submit_button.click()

   @then("I should see a success message")
   def step_check_success_message(context):
       # Implement code to check if a success message is displayed on the page
       success_message_element = context.driver.find_element(By.ID, "successMessage")
       assert success_message_element.is_displayed()
   ```

   

4. **Run Behave Tests**:
   Open your command prompt or terminal, navigate to the directory where your feature files and step definitions are located, and run the following command:

   ```bash
   behave
   ```

   Behave will execute the Gherkin scenarios and map them to the corresponding step definitions, reporting the results of each scenario.

By following these steps, you can incorporate BDD with Behave and Gherkin into your Selenium tests for the Flask application. This approach enhances collaboration, clarifies requirements, and ensures your application behaves as expected based on the defined scenarios.


<!-- MARKDOWN LINKS & IMAGES  -->

[contributors-shield]: https://img.shields.io/github/contributors/mssalstrom/Group5-repo-projects
[contributors-url]: https://github.com/mssalstrom/Group5-repo-projects/graphs/contributors
[commit-shield]: https://img.shields.io/github/last-commit/mssalstrom/Group5-repo-projects
[pypi-shield]: https://img.shields.io/pypi/pyversions/iconsdk



