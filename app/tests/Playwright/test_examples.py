import pytest
import re
from playwright.sync_api import sync_playwright, expect


def test_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://www.google.com')
        page.screenshot(path='test_screenshot.png')


def test_web_interaction():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://www.saucedemo.com/')
        page.fill('input[id="user-name"]', 'standard_user')
        page.fill('input[id="password"]', 'secret_sauce')
        page.click('input[name="login-button"]')
        expect(page.get_by_text('Products')).to_be_visible()
        browser.close()


def test_response():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        response = page.request.get('https://www.saucedemo.com/')
        expect(response).to_be_ok()


def test_submit_fail():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://www.saucedemo.com/')
        page.click('input[name="login-button"]')
        expect(page.locator("h3")).to_have_text("Epic sadface: Username is required")
        page.screenshot(path='sumbit_fail.png')

