from behave import *
import selenium
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

"""RTM REFERENCE: File Name Shortener TC3, TC4"""


@when('I enter file "{file}"')
def enter_url(context, file):
    context.driver.find_element(By.ID, "fileInput").send_keys(os.path.join(os.getcwd(), "tests\\", file))


@when('I enter shortened name "{sn}"')
def enter_short_name(context, sn):

    context.driver.find_element(By.ID, "codeName").send_keys(sn)


@when('I select the save file button')
def press_button(context):
    context.driver.find_element(By.ID, "saveImage").click()






