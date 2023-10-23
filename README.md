

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
- [Setup](#setup)
- [Lab](#Lab)
- [Basics](#Basics)
- [UnitTest](#UnitTest)


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

# Lab 
Below are a series of test in the selenium suite of tools that can be used to automate test for a python web application. 

- Create a new python file named "seleniumLab.py" in the test directory. 

### Basics
1. Using Selenium to test link navigation:  
- Import libraries
```cmd
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
```


- #### Create webdriver object and set window size
```cmd
driver = webdriver.Edge()
```
```cmd
driver.set_window_size(800,800)
```
```cmd
local_url = "localhost:5000"
```

- #### Launching link: 
```cmd
driver.get(local_url)
```


&#160;&#160;&#160;Expected outcome: *browser should navigate to link*

2. Using Selenium to find elements:  

```cmd
url_element = driver.find_element(By.NAME, "url")
```
```cmd
code_element = driver.find_element(By.NAME, "code")
```
```cmd
submit_button = driver.find_element(By.ID, "shortenSubmit")
```
3. Using Selenium to test website functionality:  

- Clear preexisitng text and type python.org into url shortener
```cmd
url_element.clear()
```
```cmd
url_element.send_keys("https://python.org")
```

- Clear preexisitng text and type python as shortened url
```cmd  
code_element.clear()
```

```cmd
code_element.send_keys("python")
```
- Click submit

```cmd
submit_button.click()
```


- Wait 10s to verify page
```cmd
time.sleep(10)
```
- Go back to homepage

- Testing file input 
```cmd
driver.get(local_url)
```
```cmd
fileElement = driver.find_element(By.ID, "fileInput")
```
```cmd
fileElement.send_keys(file_path)
```
```cmd
codeNameElement = driver.find_element(By.ID, "codeName")
```
```cmd
codeNameElement.send_keys("Shortname")
```
```cmd
time.sleep(10)
```


- Retesting with longer URL
- Clear preexisitng text and type python.org into url shortener
```cmd
url_element.clear()
```
```cmd
url_element.send_keys("[https://python.org](https://www.cnn.com/2023/02/09/us/iyw-puppy-bowl-shelters-rescue-groups/index.html)")
```

- Clear preexisitng text and type python as shortened url
```cmd  
code_element.clear()
```

```cmd
code_element.send_keys("puppyBowl")
```
- Click submit

```cmd
submit_button.click()
```


- Wait 10s to verify page
```cmd
time.sleep(10)
```
- Go back to homepage
  
```cmd
driver.get(local_url)
```
- Testing file input
```cmd
fileElement = driver.find_element(By.ID, "fileInput")
```
```cmd
fileElement.send_keys(file_path)
```
```cmd
codeNameElement = driver.find_element(By.ID, "codeName")
```
```cmd
codeNameElement.send_keys("Shortname")
```
```cmd
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

```cmd
class urlShortener(unittest.TestCase):
```
- Initialize the webdriver
```cmd
    def setUp(self):
        self.driver = webdriver.Edge()
```
- Declare the test case method
```cmd
    def test_urlShortener(self):
```
- Set the driver
```cmd
        driver = self.driver
```
- Navigate to web application
```cmd
        driver.get("localhost:5000")
```
- Assertion to confirm site title
```cmd
        self.assertIn("urlShortener", driver.title)
```
- locate elements in page
```cmd
        url_element = driver.find_element(By.NAME, "url")
        code_element = driver.find_element(By.NAME, "code")
        submit_button = driver.find_element(By.ID, "shortenSubmit")

```
- Send data
```cmd
        url_element.clear()
        url_element.send_keys("https://python.org")
        submit_button.click()

        
```
- Wait to verify page
```cmd
        time.sleep(10)   
```
- Close driver
```cmd
    def tearDown(self):
        self.driver.close()
```
- Execute test
```cmd
if __name__ == "__main__":
    unittest.main()
```


<!-- MARKDOWN LINKS & IMAGES  -->

[contributors-shield]: https://img.shields.io/github/contributors/mssalstrom/Group5-repo-projects
[contributors-url]: https://github.com/mssalstrom/Group5-repo-projects/graphs/contributors
[commit-shield]: https://img.shields.io/github/last-commit/mssalstrom/Group5-repo-projects
[pypi-shield]: https://img.shields.io/pypi/pyversions/iconsdk



