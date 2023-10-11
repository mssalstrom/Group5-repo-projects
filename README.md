

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
- [Lab](#Lab)


<!-- ABOUT THE PROJECT -->
# Introduction
### Purpose 
> This document provides detailed instructions for testing a provided web application using selenium. Selenium is a library and suite of tools used to build test for web applications.

### Tools Used: 
- Python
- Selenium
- Flask

### Contributer Roles
- Dmytro Holovnia - Developer
- Matthew Salstrom - Developer
- Max Tart - Developer
- Dylan Arone - Tester
- Ian Kepplinger - Tester
- Ever Morales Alverez Tester
- Denitri Douglas - Document Writer
- Keven Hernandez Gaspar - Document Writer
- Eric Dixon - Document Writer
    



# Setup
Create a new python file named "seleniumLab.py" preferably in a virtual environment. 

### Installing Flask: 
>In python terminal
```cmd
pip install -r requirements.txt
```
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
# Lab 

### Using Selenium to test link navigation:  
import web driver
```cmd
from selenium import webdriver
```
#### create webdriver object
```cmd
driver = webdriver.Edge()
```


#### launching link: 
```cmd
driver.get(link or path)
```


**Expected outcome: browser should navigate to link

<!-- MARKDOWN LINKS & IMAGES  -->

[contributors-shield]: https://img.shields.io/github/contributors/mssalstrom/Group5-repo-projects
[contributors-url]: https://github.com/mssalstrom/Group5-repo-projects/graphs/contributors
[commit-shield]: https://img.shields.io/github/last-commit/mssalstrom/Group5-repo-projects
[pypi-shield]: https://img.shields.io/pypi/pyversions/iconsdk



