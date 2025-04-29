
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")          # Enable incognito mode
    chrome_options.add_argument("--disable-notifications")  # Disable notifications
    chrome_options.add_argument("--start-maximized")    # Maximize the window

    # Initialize the browser
    driver = webdriver.Chrome(options=chrome_options)

    # Open the login page
    driver.get('https://www.saucedemo.com/')
    
    # Wait for 3 seconds before every action
    time.sleep(3)

    # Wait and locate the username field
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
    )
    time.sleep(3)
    # Enter incorrect username
    username_field.send_keys('incorrect_user')

    # Wait and locate the password field
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
    )
    time.sleep(3)
    # Enter valid password
    password_field.send_keys('secret_sauce')

    # Wait and locate the login button
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]'))
    )
    time.sleep(3)
    # Click the login button
    login_button.click()

    # Wait and verify the error message is displayed
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@data-test="error"]'))
    )

    assert error_message.is_displayed(), "Error message not displayed."
    print("Test case passed.")
    sys.exit(0)

except Exception as e:
    print(f"Test case failed: {e}")
    sys.exit(1)

finally:
    # Close the browser
    driver.quit()
