
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

# Setting up Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--start-maximized")

# Initializing WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the homepage
    driver.get('https://www.saucedemo.com/')
    
    # Define a function for waiting and locating elements
    def wait_for_element(xpath):
        time.sleep(3)
        return driver.find_element(By.XPATH, xpath)
    
    # Step 1: Navigation to Login Page
    # (Since we directly navigate to the login page, this step is inherently completed)

    # Step 2: Entering username
    username_field = wait_for_element('//*[@id="user-name"]')
    username_field.send_keys('user123')

    # Step 3: Entering incorrect password
    password_field = wait_for_element('//*[@id="password"]')
    password_field.send_keys('incorrectPasswd')

    # Step 4: Clicking the 'Login' button
    login_button = wait_for_element('//*[@id="login-button"]')
    login_button.click()

    # Step 5: Validating error message
    time.sleep(3)
    error_message = wait_for_element('//div[contains(@class, "error-message-container")]//h3')
    if "Epic sadface: Username and password do not match any user in this service" in error_message.text:
        print("Test Case Passed")
        sys.exit(0)
    else:
        print("Test Case Failed: Error message did not match")
        sys.exit(1)
        
except Exception as e:
    print(f"Test Case Failed due to Exception: {e}")
    sys.exit(1)
finally:
    # Close and quit the driver
    driver.quit()
