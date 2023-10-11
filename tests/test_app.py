import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

local_url = "localhost:5000"
file_path = os.path.join(os.getcwd(), "File.txt")

#I didn't put this in pytest/unittest form so I could focus on making sure I am using selenium right
#I'd be happy to fix that but I wanted to go over it in code review first

#selenium driver setup

driver = webdriver.Firefox()
driver.set_window_size(800,800)
driver.get(local_url)

# Part 1: basic url - intended input
#Works as intended after slight fixes to app.py

url_element = driver.find_element(By.NAME, "url")
code_element = driver.find_element(By.NAME, "code")
submit_button = driver.find_element(By.ID, "shortenSubmit")

#clear preexisitng text and type python.org into url shortener
url_element.clear()
url_element.send_keys("https://python.org")
#clear preexisitng text and type python as shortened url
code_element.clear()
code_element.send_keys("python")
#click submit
submit_button.click()

#wait 10s to verify page
time.sleep(10)
#go back to homepage
driver.get(local_url)

# Part 2: file input - intended input
#Works as intended after slight fixes to app.py

fileElement = driver.find_element(By.ID, "fileInput")
fileElement.send_keys(file_path)

codeNameElement = driver.find_element(By.ID, "codeName")
codeNameElement.send_keys("Shortname")

saveImageElement = driver.find_element(By.ID, "saveImage")
saveImageElement.click()

#wait 10s to verify page
time.sleep(10)

