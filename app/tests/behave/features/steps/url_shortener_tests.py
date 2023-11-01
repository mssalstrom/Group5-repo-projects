from behave import *
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

"""RTM REFERENCE: URL Shortener TC1, TC2"""


@when('I enter url "{url}"')
def enter_url(context, url):
    context.driver.find_element(By.NAME, "url").send_keys(url)


@when('I enter shorten name "{sn}"')
def enter_short_name(context, sn):

    context.driver.find_element(By.NAME, "code").send_keys(sn)


@when('I select the shorten URL button')
def press_button(context):
    context.driver.find_element(By.ID, "shortenSubmit").click()







