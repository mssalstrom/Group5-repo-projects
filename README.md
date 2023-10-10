

``` mermaid
flowchart TD;
    test1((Test1))
    test2(Test2)
    test1-->test2
```

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
![Commits][commit-shield]
![pypi-shield]






<br />
<div align="center">
    <h3 align="center">CSC 256 Group 5 Project Readme</h3>
</div>



<!-- TABLE OF CONTENTS -->

# Table of Contents:
- [Introduction](#Introduction)
- [Setup](#setup)


<!-- ABOUT THE PROJECT -->
# Introduction
### Purpose 
> This document provides detailed instructions for testing a provided web application using selenium. Selenium is a library and suite of tools used to build test for web applications.

### Tools Used: 
- Python
- Selenium
- Flask



# Setup

### Installing Flask: 
>In python terminal

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
# Using Selenium 

#### Navigating to link: 
import web driver
```cmd
from selenium import webdriver
```
#### create webdriver object
```cmd
driver = webdriver.Edge()
```


### lauching link: 
```cmd
driver.get(link or path)
```


**Expected outcome: browser should navigate to link

<!-- MARKDOWN LINKS & IMAGES  -->

[contributors-shield]: https://img.shields.io/github/contributors/mssalstrom/Group5-repo-projects
[contributors-url]: https://github.com/mssalstrom/Group5-repo-projects/graphs/contributors
[commit-shield]: https://img.shields.io/github/last-commit/mssalstrom/Group5-repo-projects
[pypi-shield]: https://img.shields.io/pypi/pyversions/iconsdk



