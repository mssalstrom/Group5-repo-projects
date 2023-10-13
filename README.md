

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

- In your python IDE open the app project
- Open the file app.py
  
>In python terminal
```cmd
pip install -r requirements.txt
```

### Installing Flask: 
```cmd
pip install flask
```
### Test Flask installation: 
launch repl
```cmd
python
```
```cmd
import flask
```
```cmd
exit()
```
* Expected outcome: there should be no errors following the import command if flask has been installed correctly

### Installing Selenium: 
>In python terminal

On Windows: 
```cmd
python -m pip install selenium
```
On Mac 
```cmd
pip3 install selenium
```
### Test Selenium installation: 
launch repl
```cmd
python
```
```cmd
import selenium
```
```cmd
exit()
```
* Expected outcome: there should be no errors following the import command if selenium has been installed correctly

- Run the application app.py.
- In the python terminal you will see " *Running on http://127.0.0.1:5000 "
- Select the hyperlink to launch the web application
- If you launch the web application "URL Shortener" you have set up the lab correctly. Review the above steps to install the flask and selenium libraries as needed. 
  
# Lab 
Below are a series of test in the selenium suite of tools that can be used to automate test for a python web application. 

-Create a new python file named "seleniumLab.py" in the test directory. 

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


**Expected outcome: browser should navigate to link

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



