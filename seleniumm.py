# Working with selenium

'''
1 - pipenv install selenium (Need to install selenium to work with it)
2 - Need to install "Driver" ("driver" is a piece of software to automate the specific browser)
    2.1 - Go to Pypi -> search selenium -> scroll down
    2.2 - Below we find different "drivers" for different browsers like chrome, firefox, edge, etcs
    2.3 - Click on the respective browser driver link you wanna use for your script (I selected chrome)
    2.4 - Clikc on the latest/current release driver link
    2.5 - Download the chromedriver according the to the os (for windows)
    2.6 - Will get a "zipfile". -> extract the zipfile
    2.7 - Move or copy the chromedriver in "c drive" if using windows. (We need to put it somewhere in the path)
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

chromeOption = webdriver.ChromeOptions()
#chromeOption.add_experimental_option("excludeSwitches", ['enable-automation'])
#chromeOption.add_experimental_option("excludeSwitches", ['enable-logging'])

# This make chrome window to stay open
chromeOption.add_experimental_option("detach", True)

browser = webdriver.Chrome(
    executable_path=".chromedriver.exe", options=chromeOption)

browser.get("https://github.com")

# Telling selenium to find 'sign in' element on github page and click it (finding by text)
singin_link = browser.find_element(By.LINK_TEXT, "Sign in")
singin_link.click()

# Now we need to fill the username & password fields
username_box = browser.find_element(
    By.XPATH, "//form/input[@id='login_field']")

# "send_keys()" let's you fill the username box, it's stimulates the a user typing in text box
username_box.send_keys("dk11-testing")

password_box = browser.find_element(
    By.XPATH, "//form/div/input[@id='password']")
password_box.send_keys("dktesting@github")

submit = browser.find_element(By.XPATH, "//form/div/input[@type='submit']")
submit.click()
