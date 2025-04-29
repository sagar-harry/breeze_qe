
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import sys

# Setting up the Chrome options to run in incognito mode and disable notifications
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")

# Launching the Chrome browser
driver = webdriver.Chrome(options=chrome_options)

try:
    # Maximize the browser window
    driver.maximize_window()

    # Navigate to the homepage
    driver.get("https://www.saucedemo.com/")

    # Step 1: Wait for the page to load and be on the login page
    time.sleep(3)

    # Step 2: Enter a valid username
    username_field = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    username_field.clear()
    username_field.send_keys("standard_user")

    # Step 3: Enter an incorrect password
    time.sleep(3)
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_field.clear()
    password_field.send_keys("wrong_password")

    # Step 4: Click the 'Login' button
    time.sleep(3)
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()

    # Step 5: Wait for the error message and verify it
    time.sleep(3)
    error_message_displayed = False

    try:
        error_message = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        if "Epic sadface: Username and password do not match any user in this service" in error_message.text:
            error_message_displayed = True
    except NoSuchElementException:
        error_message_displayed = False

    # Check if the error message was displayed as expected
    if error_message_displayed:
        sys.exit(0)
    else:
        sys.exit(1)

except Exception as e:
    print(f"An exception occurred: {e}")
    sys.exit(1)
finally:
    # Clean up and close the browser
    driver.quit()
