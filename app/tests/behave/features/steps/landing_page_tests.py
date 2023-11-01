from behave import *
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@then('I verify that the logo is present on page')
def check_logo(context):
    context.driver.find_element(By.ID, 'wtccHeaderImage')




